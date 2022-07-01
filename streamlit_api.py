import pickle
import streamlit as st

pickle_in = open('clf.pkl', 'rb')
classifier = pickle.load(pickle_in)

def welcome():
    return "The Bank Authentication app WELCOMES you"

def pedict_note(variance, skewness, curtosis, entropy):
    
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    return prediction

def main():
    st.title("Bank Note Authentication")
    html_temp = """
    <div style = "background-color:blue;padding:10px">
    <h2 style = "color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("variance", "Type Here")
    skewness = st.text_input("skewness", "Type Here")
    curtosis = st.text_input("curtosis", "Type Here")
    entropy = st.text_input("entropy", "Type Here")
    result=""
    
    if st.button("Predict"):
        result = pedict_note(variance, skewness, curtosis, entropy)
    st.success(f"The output is {result}")
    
if __name__ =="__main__":
    main()
