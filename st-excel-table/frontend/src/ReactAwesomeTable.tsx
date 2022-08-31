import React from "react"
import { RenderData } from "streamlit-component-lib";
import { useRenderData } from "streamlit-component-lib-react-hooks";
import { Table, TableProps } from '@tk42/react-awesome-table';


const ReactAwesomeTable: React.FC = () => {
    const renderData: RenderData = useRenderData()
    const args: TableProps<any> = renderData.args

    const [data, setData] = React.useState<Partial<any>[]>(args.data);
    const handleChange = React.useCallback((items: Partial<any>[]) => {
        setData(items);
    }, []);
    const getRowKey = React.useCallback((item: any | undefined, rowIndex: number): string => {
        return `${String(item)}_${rowIndex}`;
    }, []);

    return (
        <Table
            data={data}
            columns={args.columns}
            getRowKey={getRowKey}
            onChange={handleChange}
            options={args.options}
        />
    )
};

export default ReactAwesomeTable;
