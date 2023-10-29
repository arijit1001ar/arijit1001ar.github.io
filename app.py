import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_blog1 = Image.open("images/Library.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Arijit :wave:")
    st.title("A Data Architect From Canada")
    st.write(
        "I am passionate about the world of data and metadata."
    )
   # st.write("[Learn More >](https://pythonandvba.com)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
           Hello I'm Arijit, a passionate IT professional currently working for IBM Consulting, Canada. As a data architect I bring a wealth of experience and expertise to the table. My recent years are spent exploring the intricacies of Salesforce helping businesses harness its capabilities to drive growth and success.

As a seasoned professional within the IT industry I am well-versed in the nuances of data architecture ensuring that companies have robust and scalable solutions in place to effectively manage their data. Through careful analysis strategic planning and seamless integration I strive to optimize processes and empower businesses to make data-driven decisions.

Throughout my career I have collaborated with cross-functional teams advising on best practices designing data models and implementing customized solutions tailored to meet specific business needs. I am adept at navigating the Salesforce ecosystem and leveraging its vast array of tools and functionality to unlock the full potential of data.

In addition to my technical expertise I am a keen problem-solver and a proactive communicator recognizing the importance of bridging the gap between technical jargon and functional requirements. Through my blog I aim to share insights tips and strategies to help individuals and businesses navigate the complexities of Salesforce data architecture.

Whether you are a Salesforce administrator, developer or a business owner looking to leverage the power of data my blog will provide you with valuable resources and information to guide your journey.
            """
        )
        st.write("[My LinkedIn URL >](https://www.linkedin.com/in/arijitraysalesforcedataarchitect)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Blogs")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_blog1)
    with text_column:
        st.subheader("Salesforce Library Migration")
        st.write(
            """
           Read to learn about Salesforce Library Migration process. 
           You will learn about Content management in Salesforce and understand the steps for migrating the library contents of one Salesforce Org to another.
            """
        )
        st.markdown("[Read my Blog...](https://www.apexhours.com/salesforce-library-migration-process-2/)")


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/arijit1001.ar@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
