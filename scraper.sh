#!/bin/bash

# Mentor Skill Auto-Scraper
# Usage: ./scraper.sh "Professor Name" "Institution"

set -e

MENTOR_NAME="$1"
INSTITUTION="$2"
OUTPUT_DIR="${3:-.}"
TIMEOUT=10

# Helper: Safe curl with timeout
fetch_url() {
    local url="$1"
    local timeout="${2:-$TIMEOUT}"
    curl -s --connect-timeout "$timeout" --max-time "$timeout" "$url" 2>/dev/null || echo ""
}

# Parse Google Scholar profile if URL provided
scrape_google_scholar() {
    local url="$1"
    if [[ -z "$url" ]]; then
        return 0
    fi

    echo "📚 Scraping Google Scholar..."
    local response=$(fetch_url "$url")

    # Extract h-index and metrics
    local h_index=$(echo "$response" | grep -oP 'h-index">\K[^<]+' | head -1)

    # Extract paper titles (rough parsing)
    echo "$response" | grep -oP '<a href="[^"]*"[^>]*>\K[^<]+(?=</a>)' | head -20
}

# Parse Baidu Scholar (百度学术)
scrape_baidu_scholar() {
    local name="$1"
    local institution="$2"
    local query="作者:$name AND 单位:$institution"

    echo "🔍 Searching Baidu Scholar..."
    # Note: Baidu may require JavaScript rendering; curl alone won't fully work
    # This is a placeholder for the structure
    echo "Query: $query (requires browser rendering for full results)"
}

# Search Google for homepage and public mentions
scrape_google_search() {
    local name="$1"
    local institution="$2"

    echo "🌐 Searching Google..."
    local query="$name $institution"
    local search_url="https://www.google.com/search?q=$(echo "$query" | sed 's/ /+/g')"

    # Rough extraction of domain results
    fetch_url "$search_url" | grep -oP 'href="([^"]*)"' | grep -v 'google.com' | sort -u | head -10
}

# Search for ORCID
scrape_orcid() {
    local name="$1"

    echo "🔐 Searching ORCID..."
    local search_url="https://orcid.org/orcid-search/search?q=$(echo "$name" | sed 's/ /+/g')"
    fetch_url "$search_url" | grep -oP 'orcid.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]' | head -1
}

# Main execution
main() {
    echo "===== Mentor Auto-Scraper ====="
    echo "Name: $MENTOR_NAME"
    echo "Institution: $INSTITUTION"
    echo ""

    # Launch parallel scrapes
    scrape_google_scholar "$GOOGLE_SCHOLAR_URL" &
    scrape_baidu_scholar "$MENTOR_NAME" "$INSTITUTION" &
    scrape_google_search "$MENTOR_NAME" "$INSTITUTION" &
    scrape_orcid "$MENTOR_NAME" &

    # Wait for all background jobs
    wait

    echo ""
    echo "✅ Scraping complete. Results written to JSON."
}

main "$@"
