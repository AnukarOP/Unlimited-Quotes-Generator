import streamlit as st
import requests
import time
import base64

def fetch_quote():
    response = requests.get("https://api.quotable.io/random")
    data = response.json()
    return data['content'], data['author']

def main():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.pexels.com/photo/3178786/download/");
             background-attachment: fixed;
             background-size: cover;
             position: relative;
         }}
         .github-icon {{
             position: absolute;
             bottom: 20px;
             left: 50%;
             transform: translateX(-50%);
         }}
         .github-icon img {{
             border-radius: 50%;
             width: 100px;
             height: 100px;
             box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
         }}
         </style>
         """,
         unsafe_allow_html=True
    )

    st.markdown('<a class="github-icon" href="https://github.com/AnukarOP"><img src="https://i.ibb.co/vJS3PBG/wallpapersden-com-dc-joker-art-512x512.jpg"></a>', unsafe_allow_html=True)

    quote_display = st.empty() # Create an empty element to hold the quote text
    quote, author = fetch_quote()

    quote_display.write(f"<h1>{quote} — {author}</h1>", unsafe_allow_html=True)
    countdown = 5
    countdown_display = st.text(f"Next quote in {countdown}")
    while True:
        while countdown > 0:
            countdown_display.text(f"Next quote in {countdown}")
            time.sleep(1) # Wait for 1 second
            countdown -= 1
        countdown = 5
        quote, author = fetch_quote()
        quote_display.write(f"<h1>{quote} — {author}</h1>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
