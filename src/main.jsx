import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

import NovoCliente from './routes/NovoCliente.jsx'
import Cliente from './routes/Cliente.jsx'

import { createBrowserRouter, RouterProvider, Route } from 'react-router-dom'

const router = createBrowserRouter([
  {
    element: <App />,
    children: [
      {
        path: "/",
      },
      {
        path: "/clientes",
        element: <Cliente/>,
      },
      {
        path: "/NovoCliente",
        element: <NovoCliente/>,
      }
    ],
  },
])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
