import streamlit as st
 
# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        path = "cdac.png"
        image = Image.open(path)
        st.image(image, width = 150)
        
local_css("style.css")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("HELLO, WELCOME TO OUR SITE :wave:")
    st.title("A BIG DATA TEAM FROM CDAC BANGLORU")
    st.write(
        """We are passionate about finding ways to use Python and BIG DATA .  
           We are aslo provide solutions for Big Data/ML.
        """
    )
    
        
 


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Us!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
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
        
