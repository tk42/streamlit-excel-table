import React from "react"
import ReactDOM from "react-dom"
import ReactAwesomeTable from "./ReactAwesomeTable"
import { StreamlitProvider } from "streamlit-component-lib-react-hooks"


ReactDOM.render(
    <React.StrictMode>
        <StreamlitProvider>
            <ReactAwesomeTable />
        </StreamlitProvider>
    </React.StrictMode>
    , document.getElementById("root"))
