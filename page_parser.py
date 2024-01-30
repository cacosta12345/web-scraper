from bs4 import BeautifulSoup

def parse_citations_needed_count(markup):
    soup = BeautifulSoup(markup, "html.parser")
    citations_needed = soup.find_all("a", href=True, title="Wikipedia:Citation needed")
    return len(citations_needed)

def parse_citations_needed_report(markup):
    soup = BeautifulSoup(markup, "html.parser")
    citations_needed = soup.find_all("a", href=True, title="Wikipedia:Citation needed")
    report = []
    for citation in citations_needed:
        parent_paragraph = citation.find_parent("p")
        if parent_paragraph:
            # Ensure each citation is separated clearly.
            report.append(parent_paragraph.text.strip() + "\n")
    return "\n".join(report)

