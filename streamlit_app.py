# -*- coding: utf-8 -*-
"""오프라인 재고 정체 현황 리포트 - Streamlit Community Cloud 배포용"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

BASE = Path(__file__).parent
HTML = BASE / "index.html"
PDF = BASE / "offline-inventory-report.pdf"

st.set_page_config(page_title="오프라인 재고 정체 현황",
                   page_icon="📦", layout="wide")

st.markdown("""
<style>
  .block-container{padding:0.6rem 1rem 2rem;max-width:1180px}
  header[data-testid="stHeader"]{background:transparent}
  #MainMenu,footer{visibility:hidden}
</style>
""", unsafe_allow_html=True)

if PDF.exists():
    st.download_button("PDF 내려받기", PDF.read_bytes(),
                       file_name="오프라인_재고정체_보고.pdf",
                       mime="application/pdf")

html = HTML.read_text(encoding="utf-8")
# 앱 안에서는 Streamlit 다운로드 버튼을 쓰므로 리포트 내부 링크는 숨긴다
html = html.replace('<a class="dl"', '<a class="dl" style="display:none"')

components.html(html, height=7200, scrolling=True)
