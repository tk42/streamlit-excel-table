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
            options={args.options ?? { "sortable": false, "filterable": false }}
            rowsPerPage={args.rowsPerPage ?? 10}
            rowsPerPageOptions={args.rowsPerPageOptions ?? [10, 30, 100]}
            readOnly={args.readOnly ?? false}
            sticky={args.sticky ?? false}
            rowNumber={args.rowNumber ?? false}
            disableUndo={args.disableUndo ?? false}
        />
    )
};

export default ReactAwesomeTable;
