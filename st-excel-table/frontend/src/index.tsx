import React from "react"
import ReactDOM from "react-dom"
import ReactAwesomeTable from "./ReactAwesomeTable"
// import EmptyRow from './empty'
import { StreamlitProvider } from "streamlit-component-lib-react-hooks"


ReactDOM.render(
    <React.StrictMode>
        <StreamlitProvider>
            < ReactAwesomeTable />
            {/* <EmptyRow /> */}
        </StreamlitProvider>
    </React.StrictMode>
    , document.getElementById("root"))
