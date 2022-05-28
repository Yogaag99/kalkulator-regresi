from math import sqrt
from turtle import color, textinput
from PIL import Image
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.title('KALKULATOR REGRESI')

st.header('Input Data')
data = ''
user_know = False
with st.form(key='my_form'):
    data = st.text_area('Masukkan data x dan y dengan format seperti pada contoh')
    submit_button = st.form_submit_button('Submit')
    if submit_button:
        user_know = True

contoh = st.empty()

with contoh.container():
    st.text('Contoh')
    cth_ketik = Image.open('contoh-ketik.PNG')
    st.image(cth_ketik, width=700)
    expander = st.expander('APA MAKSUDNYA ITU?')
    cth_data = Image.open('contoh-data.PNG')
    expander.text('Jika punya data seperti ini')
    expander.image(cth_data, width=300)
    expander.write('''
        Ketik datanya dengan format sebagai berikut:  
        (data x),(data y)   
        (data x),(data y)   
        (data x),(data y)   
        ...  
        ...
        ''')
    expander.warning('''
        **Perhatikan!**  
        Jangan sampai ada spasi
    ''')
    expander.write('''
        Angka ditulis dengan notasi Amerika: separator pada desimal berupa titik (.) dan pada ribuan berupa koma (,). Jadi,  
        2,374 dibaca ***dua ribu tiga ratus tujuh puluh empat ***   
        0.424 adalah hasil dari ***424 dibagi 1000*** \n
        Terbalik :thumbsup:
    ''')

st.text('\n')
if user_know:
    contoh.empty()

st.header('Setelah itu...')
st.subheader('Datamu akan tampil di sini')
chunks = data.split('\n')
t = chunks[0].split(',')
x = []
y = []

for i in range(len(chunks)):
    t = chunks[i].split(',')
    try:
        x.append(float(t[0]))
        y.append(float(t[1]))
    except:
        continue

df = pd.DataFrame([x,y])
df = np.transpose(df)
df.columns = ['x', 'y']
st.write(df.style.format("{:.4}"))
st.write('Jika data yang dimasukkan sudah benar, lanjut isi form di bawah ini. Jika masih salah, masukkan ulang data')

nama_grafik = ''
x_label = ''
y_label = ''
with st.form(key='graph_info'):
    nama_grafik = st.text_input("Nama grafik")
    x_label = st.text_input("Label sumbu x")
    y_label = st.text_input("Label sumbu y")
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        st.success('Tekan tombol "Calculate and Graph"')

startCalculate = st.button('Calculate and Graph')
slope = 0.0
intercept = 0.0

if startCalculate:
    contoh.empty()

    n = df.shape[0]
    df['xy'] = [df['x'][i]*df['y'][i] for i in range(n)]
    df['x^2'] = [df['x'][i]**2 for i in range(n)]
    df['y^2'] = [df['y'][i]**2 for i in range(n)]
    st.write('Data untuk kalkulasi regresi linier', df.style.format("{:.4}"))

    sum_x = sum(df['x'])
    sum_y = sum(df['y'])
    sum_xy = sum(df['xy'])
    sum_xx = sum(df['x^2'])
    sum_yy = sum(df['y^2'])

    delta = n*sum_xx - sum_x**2

    slope = (n*sum_xy - sum_x*sum_y)/delta
    intercept = (sum_xx*sum_y - sum_x*sum_xy)/delta

    S_y = sqrt(1/(n-2) * (sum_yy - (sum_xx*sum_y**2 - 2*sum_x*sum_xy*sum_y + n*sum_xy**2)/delta))
    d_slope = sqrt(n/delta) * S_y
    d_intercept = sqrt(sum_xx/delta) * S_y

    st.text('Persamaan regresi linier')
    st.latex(rf'y = {round(slope, 3)}x + {round(intercept, 3)}')
    st.text(f'slope: {slope}')
    st.text(f'intercept: {intercept}')

    fig, ax = plt.subplots()
    ax.scatter(x,y)
    p1 = slope*x[0] + intercept
    p2 = slope*x[-1] + intercept
    ax.plot([x[0], x[-1]], [p1, p2], linestyle='dashed', color='green')
    ax.set_title(nama_grafik)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    st.pyplot(fig)