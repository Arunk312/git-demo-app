import streamlit as st

st.title('Pg')

col1,col2, col3 = st.columns(3)

with col1:
    st.image('cuty2.jpg',width=300)

with col2:
    st.write('One of my noughty student')

with col3:
    st.write(' she is bad at studey , i can imagin where is study  will take her')


st.header('courses')
st.header('Data science')
st.sidebar.title('menu')
st.sidebar.markdown("""
- Home
- about 
- contect
- career
- logine                    
""")
st.sidebar.write('sidebar create ot test delete branch')
