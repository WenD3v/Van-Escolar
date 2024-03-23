import React from 'react';
import { Menu } from 'antd';
import { Link } from 'react-router-dom';
import {AppstoreOutlined,FallOutlined,RiseOutlined,UserAddOutlined,CarOutlined,IdcardOutlined,LineChartOutlined} from '@ant-design/icons';

const MenuList = ({darkTheme}) => {
  return <Menu theme={darkTheme ? 'dark':'light'} mode='inline' className='menu-bar'>
        <Menu.Item key="dashboard" icon={<AppstoreOutlined/>}>
            Dashboard
        </Menu.Item>
        <Menu.Item key="cliente" icon={<UserAddOutlined/>}>
            <Link to="/clientes">Clientes</Link>
        </Menu.Item>
        <Menu.SubMenu title="Finanças" key="finances" icon={<LineChartOutlined/>}>
            <Menu.Item key="contaspagar" icon={<FallOutlined/>}> Contas a Pagar</Menu.Item>
            <Menu.Item key="contasreceber" icon={<RiseOutlined/>}> Contas a Receber</Menu.Item>
        </Menu.SubMenu>
        
    
        <Menu.Item key="veiculo" icon={<CarOutlined/>}>
            Veiculos
        </Menu.Item>
        <Menu.Item key="motorista" icon={<IdcardOutlined/>}>
           Motorista
        </Menu.Item>
    </Menu>
  
}

export default MenuList