import { useState,useEffect } from "react"
import { Link } from "react-router-dom"
import axios from "axios"
import './Home.css'


const Home = () => {
    const [contas,setContas] = useState([])
    const getContas = async() => {
        try {
            const response = await axios.get("http://192.168.15.4:5000/contas_receber/");
            const data = response.data;
            setContas(data);

        } catch (error) {
            console.log(error)
        }
    }
    useEffect(()=>{
        getContas()
    },[])
    return <div>
        <h1>Contas a Receber</h1>
        {contas.length === 0 ? (<p>Carregado...</p>) : (
            contas.map((conta)=> (
                <div className="post" key={conta.ID_CONTAS_RECEBER}>
                    <h1>
                    {conta.DESCRICAO}
                    </h1>
                    <small>lançado: {conta.DATA_CADASTRO} vencimento: {conta.DATA_RECEBIMENTO}</small>
                    <Link to={`/contas/${conta.id}`} className="btn-edit">Editar</Link>
                </div>
            ))
        )}
    </div>;
}

export default Home