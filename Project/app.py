import streamlit as st
import ollama

def generate_itinerary(destination, days, nights):

    prompt = f"""
    Create a detailed travel itinerary in MARKDOWN format.

    - Start with ## Title
    - Use **Day 1:**
    - Use **Morning:**, **Afternoon:**, **Evening:**, **Night:**

    Destination: {destination}
    Duration: {days} days and {nights} nights
    """

    response = ollama.chat(
        model="tinyllama",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]


st.title(" Travel Itinerary Generator")

destination = st.text_input("Destination:")
days = st.number_input("Days:", min_value=1)
nights = st.number_input("Nights:", min_value=0)

if st.button("Generate Itinerary"):
    if destination:
        with st.spinner("Generating..."):
            result = generate_itinerary(destination, days, nights)
            st.markdown(result)
    else:
        st.error("Enter destination.")