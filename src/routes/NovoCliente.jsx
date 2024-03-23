import React from 'react'
import { UserOutlined } from '@ant-design/icons';
import { Input } from 'antd';
import { useState } from "react"
import axios from "axios"
import './NovoCliente.css'

const NovoCliente = () => {

  const [sucesso, setSucesso] = useState(false); // Estado para controlar a exibição da mensagem de sucesso

  const handleSubmit = async (event) => {
    event.preventDefault(); // Evita o comportamento padrão de envio do formulário
    const formData = new FormData(event.target); // Obtém os dados do formulário
    const clienteData = {}; // Objeto para armazenar os dados do cliente

    // Itera sobre os campos do formulário e os adiciona ao objeto clienteData
    formData.forEach((value, key) => {
      clienteData[key] = value;
    });

    // Envia a solicitação POST usando Axios
    try {
      await axios.post('http://127.0.0.1:5000/clientes/', clienteData);
      setSucesso(true); // Define o estado sucesso como true
    } catch (error) {
      console.error('Erro ao cadastrar cliente:', error);
      // Adicione aqui qualquer tratamento de erro que você queira realizar
    }
  };

  return <div>
      <h1>Cadastro de Cliente</h1>
      <form id="clienteForm" onSubmit={handleSubmit} method="POST">
        <div class="form-group">
          <label for="cpf">CPF:</label>
          <input type="text" id="cpf" name="CPF" required/>
        </div>
        <div class="form-group">
          <label for="nome">Nome:</label>
          <input type="text" id="nome" name="NOME" required/>
        </div>
        <div class="form-group">
          <label for="celular">Celular:</label>
          <input type="tel" id="celular" name="CELULAR" required/>
        </div>
        <div class="form-group">
          <label for="telefone">Telefone:</label>
          <input type="tel" id="telefone" name="TELEFONE"/>
        </div>
        <button type="submit">Cadastrar</button>
      </form>
  </div>

};

export default NovoCliente
