#!/usr/bin/env python3
"""
Mentor Skill Auto-Scraper
Scrapes public academic data from multiple sources to distill mentor profile.
"""

import json
import sys
import time
import re
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import quote, urljoin
import urllib.request
import urllib.error

# Configuration
TIMEOUT = 10
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
MAX_WORKERS = 3

class MentorScraper:
    def __init__(self, mentor_name: str, institution: str, scholar_url: str = None):
        self.mentor_name = mentor_name
        self.institution = institution
        self.scholar_url = scholar_url  # Optional pre-provided Google Scholar URL
        self.results = {
            "mentor_name": mentor_name,
            "institution": institution,
            "scraped_at": datetime.now().isoformat() + "Z",
            "sources": {},
            "extracted": {
                "papers": [],
                "research_topics": [],
                "collaborators": [],
                "h_index": None,
                "academic_style": {}
            }
        }

    def fetch_url(self, url: str) -> str:
        """Safely fetch URL content with timeout."""
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
                return response.read().decode('utf-8', errors='ignore')
        except (urllib.error.URLError, urllib.error.HTTPError, Exception) as e:
            print(f"⚠️  Failed to fetch {url}: {e}", file=sys.stderr)
            return ""

    def scrape_google_scholar(self) -> dict:
        """Scrape Google Scholar profile if URL is provided, or search."""
        print("📚 Scraping Google Scholar...")

        url = self.scholar_url
        if not url:
            # Construct search URL
            query = f'"{self.mentor_name}" {self.institution}'
            url = f"https://scholar.google.com/scholar?q={quote(query)}&hl=en"

        html = self.fetch_url(url)
        if not html:
            return {"status": "failed"}

        result = {
            "status": "success",
            "url": url,
            "scraped_at": datetime.now().isoformat() + "Z",
            "papers": [],
            "metrics": {}
        }

        # Extract h-index and other metrics (rough regex-based parsing)
        h_index_match = re.search(r'h-index.{0,50}(\d+)', html)
        if h_index_match:
            result["metrics"]["h_index"] = int(h_index_match.group(1))
            self.results["extracted"]["h_index"] = int(h_index_match.group(1))

        # Extract paper titles (look for quoted text in scholar results)
        paper_matches = re.findall(r'<h3[^>]*>.*?<a[^>]*href="[^"]*">([^<]+)</a>', html)
        result["papers"] = paper_matches[:15]  # Top 15 papers
        self.results["extracted"]["papers"].extend(paper_matches[:15])

        # Try to extract research topics from paper titles
        topics = set()
        for paper in paper_matches[:10]:
            # Simple keyword extraction
            keywords = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', paper)
            topics.update(keywords[:3])

        self.results["extracted"]["research_topics"].extend(list(topics)[:8])

        return result

    def scrape_baidu_scholar(self) -> dict:
        """Scrape Baidu Scholar (百度学术) - Chinese academic papers."""
        print("🔍 Searching Baidu Scholar...")

        query = f"作者:{self.mentor_name} 机构:{self.institution}"
        url = f"https://xueshu.baidu.com/s?wd={quote(query)}"

        html = self.fetch_url(url)
        if not html:
            return {"status": "failed"}

        result = {
            "status": "success",
            "url": url,
            "scraped_at": datetime.now().isoformat() + "Z",
            "papers": []
        }

        # Extract paper titles from Baidu Scholar results
        paper_matches = re.findall(r'<a[^>]*class="[^"]*title[^"]*"[^>]*>([^<]+)</a>', html)
        result["papers"] = paper_matches[:10]
        self.results["extracted"]["papers"].extend(paper_matches[:10])

        return result

    def scrape_google_search(self) -> dict:
        """Search Google for personal homepage and public mentions."""
        print("🌐 Searching Google...")

        query = f"{self.mentor_name} {self.institution}"
        url = f"https://www.google.com/search?q={quote(query)}"

        html = self.fetch_url(url)
        if not html:
            return {"status": "failed"}

        result = {
            "status": "success",
            "query": query,
            "scraped_at": datetime.now().isoformat() + "Z",
            "homepages": [],
            "mentions": []
        }

        # Extract URLs from search results
        url_matches = re.findall(r'href="([^"]*)"', html)
        non_google_urls = [url for url in url_matches if 'google.com' not in url and url.startswith('http')][:10]
        result["homepages"] = non_google_urls[:5]

        return result

    def scrape_orcid(self) -> dict:
        """Search ORCID for researcher profile."""
        print("🔐 Searching ORCID...")

        url = f"https://orcid.org/orcid-search/search?q={quote(self.mentor_name)}"

        html = self.fetch_url(url)
        if not html:
            return {"status": "failed"}

        result = {
            "status": "success",
            "url": url,
            "scraped_at": datetime.now().isoformat() + "Z",
            "orcid_ids": []
        }

        # Extract ORCID IDs
        orcid_matches = re.findall(r'(\d{4}-\d{4}-\d{4}-\d{3}[0-9X])', html)
        result["orcid_ids"] = list(set(orcid_matches))[:3]

        return result

    def run_all_scrapes(self) -> dict:
        """Run all scrapes in parallel."""
        print(f"\n===== Mentor Auto-Scraper =====")
        print(f"Name: {self.mentor_name}")
        print(f"Institution: {self.institution}")
        print("")

        scrape_tasks = {
            "google_scholar": self.scrape_google_scholar,
            "baidu_scholar": self.scrape_baidu_scholar,
            "google_search": self.scrape_google_search,
            "orcid": self.scrape_orcid,
        }

        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = {
                executor.submit(task): name
                for name, task in scrape_tasks.items()
            }

            for future in as_completed(futures):
                task_name = futures[future]
                try:
                    result = future.result()
                    self.results["sources"][task_name] = result
                    status = "✅" if result.get("status") == "success" else "⚠️"
                    print(f"{status} {task_name}: {result.get('status', 'unknown')}")
                except Exception as e:
                    print(f"❌ {task_name}: {e}")
                    self.results["sources"][task_name] = {"status": "error", "error": str(e)}

        return self.results

    def save_to_json(self, output_file: str):
        """Save results to JSON file."""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        print(f"\n✅ Results saved to {output_file}")

def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <mentor-name> <institution> [google-scholar-url] [output-file]")
        print(f"Example: {sys.argv[0]} 'Zhang San' 'Tsinghua University'")
        sys.exit(1)

    mentor_name = sys.argv[1]
    institution = sys.argv[2]
    scholar_url = sys.argv[3] if len(sys.argv) > 3 else None
    output_file = sys.argv[4] if len(sys.argv) > 4 else "mentor_scrape.json"

    scraper = MentorScraper(mentor_name, institution, scholar_url)
    results = scraper.run_all_scrapes()
    scraper.save_to_json(output_file)

    # Pretty-print summary
    print("\n===== Summary =====")
    print(f"Papers found: {len(results['extracted']['papers'])}")
    print(f"Research topics: {', '.join(results['extracted']['research_topics'][:5])}")
    print(f"H-index: {results['extracted']['h_index'] or 'N/A'}")

if __name__ == "__main__":
    main()
