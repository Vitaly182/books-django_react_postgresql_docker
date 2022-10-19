export const ColumnFilter = ({ column }) => {
    const { filterValue, setFilter } = column;
    return (
      <span>
        Search:{" "}
        <input
          value={filterValue || ""}
          onChange={(e) => {
            setFilter(e.target.value);
          }}
          placeholder={`Search records...`}
          style={{
            fontSize: "0.9rem",
            // margin: "1rem 0",
          }}
        />
      </span>
    );
  };
  