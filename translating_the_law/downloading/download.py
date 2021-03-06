import urllib.request

def get_case_files(case, summary_url, pdf_url, post2016):
    main_text_file = f"{case}-main-text.pdf"
    press_summary_file = f"{case}-press-summary.pdf"
    urllib.request.urlretrieve(pdf_url, main_text_file)
    if not post2016:
        urllib.request.urlretrieve(summary_url, press_summary_file)
