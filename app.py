import streamlit as st
st.title('Hi my name is nithin')

# python -m venv .venv
# .venv\Scripts\activate.bat

# pip install streamlit
# streamlit hello

# python -m streamlit run app.py
# streamlit run app.py

st.write('Hello')
st.header('Hello')
st.subheader('Hello')
st.text('Hello')
st.markdown('# Hello')
st.markdown('## Hello')
st.markdown('### Hello')
st.markdown('#### Hello')
st.success('Data is safe')
st.info('Data is received')
st.warning('Data is deleted')
st.error('Data is unsafe')
exp=ZeroDivisionError('Division not possible with 0')
st.exception(exp)
st.help(exp)
st.write(range(1,10))
st.write('range(1,10)')
st.write(1+2+3)
st.write('1+2+3')
st.text(1+2+3)
st.text('1+2+3')
st.text('range(1,10)')
st.code('x = 20 \n'
       ' for i in range(x): \n '
           '\t print(i)')

# st.checkbox('male')
# st.checkbox('female')

# st.radio('male')
# st.radio('female')

# if(st.checkbox('male')):
#     st.write('you are elgible')

# if(st.checkbox('female')):
#     st.write('you are elgible')

button=st.radio('Select',('Male','Female','prefer Not to say'))
st.write('you are :',button)
# if(button=='Male'):
    # st.write('you are : MALE')
# elif(button=='Female'):
#     st.write('you are female')
# elif(button=='prefer Not to say'):
#     st.write('you are other')

select=st.selectbox("Data Science: ",['Data Analsis','Natural Language','Web Séraping' , 'Machine'])
st.write(select)
mulselect=st.multiselect("Data Science: ",['Data Analsis','Natural Language','Web Séraping' , 'Machine','Datas'])
# st.write("you've selected:",len(mulselect),mulselect)
st.write("you've selected:",len(mulselect),'courses')

if(st.button('Submit')):
    st.write('submitted successfully')
st.slider('volume:' ,min_value=0,max_value=100,step=10)
st.text_input("Enter your UserName:",value=int)
st.text_input("Enter your password:",type='password')

st.text_area("write your intro:",max_chars=50)

st.number_input("Enter your age:" ,min_value=18,max_value=28)

st.date_input("Select your date of birth:")