from unstructured.partition.html import partition_html
 

def get_content(url):
    web_content = []
    source = url
    title = ""
    group = {'metadata': {'source': source, 'title': title}, 'page_content': ''}
    seen_titles = set()

    # ingest and preprocess webpage into Unstructured elements object
    html_page = partition_html(url=source)

    # iterate the document elements and group texts by title
    for element in html_page:
        title = str((element))
        title = title[:title.find(" ")]
        if 'unstructured.documents.html.HTMLTitle' in str(type(element)):
            if title not in seen_titles:
                seen_titles.add(title)
                # If there's already content in the group, add it to all_groups
                if group['page_content']:
                    
                    group = {'metadata': {'source': source, 'title': title}, 'page_content': ''}

            group['page_content'] += element.text
            web_content.append(group)
        elif 'unstructured.documents.html.HTMLNarrativeText' in str(type(element)):
            group['page_content'] += '. ' + element.text

    # Add the last group if it exists
    if group['page_content']:
        web_content.append(group)

    # print("\n web text content ", web_content)
    return web_content

listUrl = ["https://www.amfiindia.com/investor-corner/knowledge-center/what-are-mutual-funds-new.html",
           "https://www.amfiindia.com/investor-corner/knowledge-center/introduction-to-mutual-funds.html",
           "https://www.amfiindia.com/investor-corner/knowledge-center/history-of-MF-india.html",
           "https://www.amfiindia.com/investor-corner/knowledge-center/types-of-mutual-fund-schemes.html",
           "https://www.amfiindia.com/investor-corner/knowledge-center/knowledge-center/Direct-Plan.html",
           "https://www.amfiindia.com/investor-corner/knowledge-center/tax-corner.html"
           "https://www.amfiindia.com/investor-corner/knowledge-center/Expense-Ratio.html",
           "https://www.amfiindia.com/investor-corner/knowledge-center/risks-in-mutual-funds.html",
           "https://www.amfiindia.com/investor-corner/knowledge-center/advantages-of-investing-in-mutual-funds.html",
           "https://www.amfiindia.com/investor-corner/knowledge-center/SEBI-categorization-of-mutual-fund-schemes.html",
           "https://www.amfiindia.com/investor-corner/knowledge-center/net-asset-value.html",
           "https://www.amfiindia.com/investor-corner/knowledge-center/myth-mutual-fund.html",
           "https://www.amfiindia.com/investor-corner/knowledge-center/cut-off-timings.html"

           ]

knowledge_base = [ get_content(content) for content in listUrl ] 
# knowledge_base = get_content(listUrl[0])
print("\n \n all knowledge base",knowledge_base)