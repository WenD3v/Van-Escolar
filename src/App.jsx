import Navbar  from './components/Navbar'
import { Outlet } from 'react-router-dom'
import {MenuUnfoldOutlined,MenuFoldOutlined} from '@ant-design/icons';
import {Button, Layout} from 'antd'
import Logo from './components/Logo';
import MenuList from './components/MenuList';
import ToggleThemeButton from './components/ToggleThemeButton';
import {useState} from 'react';

const {Header, Sider} = Layout;

function App() {
  const [darkTheme, setDarkTheme] = useState(true)
  const [collapsed, setCollapsed] = useState(false)
  const toggleTheme = ()=>{
    setDarkTheme(!darkTheme)
  }
  return (
    <>
     <Layout>
      <Sider theme={darkTheme? 'dark':'light'} className='sidebar'>
        <Logo/>
        <MenuList darkTheme={darkTheme}/>
        <ToggleThemeButton darkTheme={darkTheme} toggleTheme={toggleTheme}/>
      </Sider>
      <Layout>
        <Header>
          <Button type='text' icon={collapsed ? 
            <MenuUnfoldOutlined/> : <MenuUnfoldOutlined/> }/>
        </Header>
      </Layout>
     </Layout>
    </>
  )
}

export default App
