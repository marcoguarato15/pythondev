import streamlit as st
import dados_form as df
st.title("Filmes")

nome = st.text_input("Nome do filme: ", value= "")
ano = st.number_input("Ano do filme:", min_value=1926, max_value=2025)
nota = st.slider("Nota do filme: ", min_value=0, max_value=10)
id = st.number_input("Id para alteração/ remoção", min_value=1) 

if st.button("Adicionar"):
    df.addFilme(nome, ano, nota)
    st.success("Sucesso ao adicionar Filme")

if st.button("Alterar"):
    dados = df.updFilme(id, nome, ano, nota)
    st.success(f"dados upd: {dados}")

if st.button("Remover"):
    dados = df.delFilme(id)
    st.success(f"dados del: {dados}")

filmes = df.getFilmes()
st.header("Lista de Filmes")
st.table(filmes)