import streamlit as st
import google.generativeai as gen_ai

# Configure Streamlit page settings
st.set_page_config(
    page_title="LaTeX Resume Generator",
    page_icon=":page_facing_up:",  # Favicon emoji
    layout="centered",  # Page layout option
)

# Directly set the API key here (not recommended for production)
GOOGLE_API_KEY = "AIzaSyCO7WIRmXTQUPeiARLTklKLufkZRfjfg4U"

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Define the LaTeX template as a raw string
inspired = r"""
\documentclass[11pt,a4paper,sans]{moderncv}

% ModernCV themes
\moderncvstyle{banking} % Style options: 'casual', 'classic', 'banking', 'oldstyle', 'fancy'
\moderncvcolor{purple} % Color options: 'blue', 'orange', 'green', 'red', 'purple', 'grey', 'black'

\usepackage[utf8]{inputenc}
\usepackage[scale=0.75]{geometry}
\usepackage{enumitem}

\name{Pooja}{Sinha}
\title{Data Scientist}
\address{123 Main Street}{Gurgaon}{India}
\phone[mobile]{+91~1234567890}
\email{pooja.sinha@email.com}
\homepage{www.linkedin.com/in/poojasinha}

\begin{document}

\makecvtitle

\section{Education}
\cventry{2019--2023}{Bachelor of Technology}{ABC University}{Gurgaon}{\textit{CGPA: 8.0}}{}

\section{Experience}
\cventry{2022--Present}{Data Science Intern}{Analytics Vidhya}{Gurgaon}{}{
\begin{itemize}[left=0pt,label={--}]
\item Worked on various data science projects, including:
    \begin{itemize}
    \item Sentiment analysis
    \item Fake news detection
    \item Traffic sign detection
    \item And more
    \end{itemize}
\end{itemize}}

\section{Skills}
\cvitem{Programming}{Python, R, SQL}
\cvitem{Data Analysis}{Pandas, Numpy, Matplotlib, Seaborn}
\cvitem{Machine Learning}{Scikit-learn, Keras, Tensorflow}
\cvitem{Tools}{Git, Jupyter Notebook, Tableau}
\cvitem{Languages}{English, Hindi}

\section{Projects}
\cvitem{Sentiment Analysis}{Developed a sentiment analysis model using natural language processing techniques to classify customer reviews as positive or negative.}
\cvitem{Fake News Detection}{Built a machine learning model to identify fake news articles using NLP and classification algorithms.}
\cvitem{Traffic Sign Detection}{Developed a computer vision system using deep learning algorithms to detect traffic signs in real time.}

\section{Interests}
\cvitem{Data Science}{Keeping up with the latest trends and developments in the field.}
\cvitem{Sports}{Playing cricket and badminton in my free time.}

\end{document}
"""

# Streamlit app layout
st.title("LaTeX Resume Generator")

# User input
user_description = st.text_area("Enter your details about yourself")

# Combine user input with the default prompt and LaTeX template
if st.button("Generate"):
    prompt = f"""
    build a resume using latex code for me this is my profile {user_description} use this as template to make my resume {inspired}
    """
    
    with st.spinner("Generating ATS-friendly resume LaTeX code..."):
        # Generate LaTeX code using the Gemini-Pro model
        response = model.generate_content([prompt])
        latex_code = response.text

    # Display the LaTeX code
    st.subheader("Generated LaTeX Code")
    st.code(latex_code, language="latex")
