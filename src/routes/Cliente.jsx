import { useState,useEffect } from "react"
import { Link } from "react-router-dom"
import axios from "axios"
import './Cliente.css'
import { Space, Table, Tag } from 'antd';
import { FloatButton } from 'antd';
import {PlusOutlined} from '@ant-design/icons';


const Cliente = () => {
    const dataSource = []
    const columns = [
        {
            title: "ID_CLIENTE",
            dataIndex: 'ID_CLIENTE',
            key: 'ID_CLIENTE',
        },
        {
            title: "ATIVO",
            dataIndex: 'ATIVO',
            key: 'ATIVO',
        },
        {
            title: "DATA_CADASTRO",
            dataIndex: 'DATA_CADASTRO',
            key: 'DATA_CADASTRO',
        },
        {
            title: "NOME",
            dataIndex: 'NOME',
            key: 'NOME',
        },
        {
            title: "CPF",
            dataIndex: 'CPF',
            key: 'CPF',
        },
        {
            title: "TELEFONE",
            dataIndex: 'TELEFONE',
            key: 'TELEFONE',
        },
        
        {
            title: "Ações",
            key: 'actions',
            render: (_, cliente) => (
                <Space size="middle">
                    <Link to="/clientes/editar/{cliente.ID_CLIENTE}">Editar</Link>
                    <Link to="/clientes/excluir/{cliente.ID_CLIENTE}">Excluir</Link>
                </Space>
            ),
        },
        
    ];
    const [clientes,setClientes] = useState([])
    const getClientes = async() => {
        try{
            const response = await axios.get("http://192.168.1.2:5000/clientes");
            const data = response.data;
            console.log(response)
            setClientes(data)
        }
        catch(error){
            console.log(error);
        }
    }

    useEffect(()=> {
        getClientes()
    }, []
    )
    return <div>
        
        {clientes.length === 0 ? <p>Carregando...</p> : (  
            
            <Table dataSource={clientes} columns={columns} />
            
        )}
        <div className="buttonList">
            <FloatButton icon={<PlusOutlined/>} type="default"
            shape="circle"
            description="ADICIONAR"
            style={{ right: 94, color: "green", width: '100px', height: '100px', fontSize : '30px' }}
            href="/NovoCliente"
            />
        </div>
    </div>
};

export default Cliente