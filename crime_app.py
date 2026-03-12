import streamlit as st
import project_DSA_2 as crime

#  CRIME UI

st.set_page_config(
    page_title="Crime Analytics System",
    layout="wide",
    page_icon="🕵️‍♂️"
)

def crime_header(title):
    st.markdown(
        f"""
        <div style="padding:12px;border-radius:8px;background-color:#8B0000;
                    color:white;font-size:26px;font-weight:700;
                    border-left:10px solid yellow;">
            🕵️ {title}
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <style>
        body {
            background-color: #111111;
            color: white;
        }
        .stButton>button {
            background-color: #8B0000;
            color: white;
            border-radius: 5px;
            border: 2px solid yellow;
        }
        .stTextInput>div>div>input {
            background-color: #222;
            color: white;
            border: 1px solid yellow;
        }
        .stSelectbox>div>div {
            background-color: #222 !important;
            color: white !important;
            border: 1px solid yellow;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

#  SIDEBAR NAVIGATION

st.sidebar.title("🔍 Crime System Menu")
page = st.sidebar.radio(
    "Navigate",
    [
        "Home Dashboard",
        "Search Incident",
        "Multi-Search",
        "Insert Record",
        "Delete Record",
        "Modify Record",
        "Range Query",
        "Graph Algorithms",
        "Statistics",
        "KNN Similarity",
    ]
)

data = crime.data
trees = crime.trees
NUMERIC_COLUMNS = {"year", "victim_age", "offender_age", "incident_id"}


def normalize_text_input(value: str) -> str:
    """Return title-cased input for consistent matching."""
    return value.strip().title() if value else ""


def validate_input(column, raw_value):
    """Ensure numeric columns get integers and string columns are alphabetic."""
    value = raw_value.strip()
    if column in NUMERIC_COLUMNS:
        try:
            return True, int(value), None
        except ValueError:
            return False, None, f"{column.title()} must be an integer."
    formatted = normalize_text_input(value)
    cleaned = formatted.replace(" ", "")
    if not cleaned.isalpha():
        return False, None, f"{column.title()} must contain alphabetic characters only."
    return True, formatted, None


#  1. HOME
if page == "Home Dashboard":
    crime_header("Crime Analytics Dashboard")

    st.markdown("### 📊 Dataset Overview")
    st.write(f"Total incidents: **{len(data)}**")

    st.markdown("### 🧮 Quick statistics")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Minimum victim age", crime.compute_min(data, "victim_age"))
    with col2:
        st.metric("Maximum victim age", crime.compute_max(data, "victim_age"))
    with col3:
        st.metric("Average victim age", round(crime.compute_average(data, "victim_age"), 2))
    with col4:
        st.metric("Median victim age", crime.compute_median(data, "victim_age"))

    st.markdown("---")
    st.write("Use the menu to explore search, graphs, statistics, KNN, and more.")


#  2. SEARCH INCIDENT
elif page == "Search Incident":
    crime_header("Search Incident by Column")

    if "search_results" not in st.session_state:
        st.session_state["search_results"] = None
    if "search_message" not in st.session_state:
        st.session_state["search_message"] = None

    searchable_columns = ["incident_id"] + list(trees.keys())

    column = st.selectbox("Choose a column", searchable_columns)
    key = st.text_input("Enter value")
    if column not in NUMERIC_COLUMNS:
        key = normalize_text_input(key)

    if st.button("Search"):
        valid, key_cast, err = validate_input(column, key)
        if not valid:
            st.session_state["search_results"] = None
            st.session_state["search_message"] = ("error", err)
        else:
            if column == "incident_id":
                record = data.get(key_cast)
                if not record:
                    st.session_state["search_results"] = None
                    st.session_state["search_message"] = (
                        "error",
                        f"No incident found with ID {key_cast}."
                    )
                else:
                    st.session_state["search_results"] = {"ids": [key_cast], "column": column, "key": key_cast}
                    st.session_state["search_message"] = (
                        "success",
                        f"Found incident ID {key_cast}."
                    )
            else:
                result, _ = crime.search(trees, column, key_cast)
                if not result:
                    st.session_state["search_results"] = None
                    st.session_state["search_message"] = (
                        "error",
                        f"No incidents found for {column} = {key_cast}."
                    )
                else:
                    st.session_state["search_results"] = {"ids": result, "column": column, "key": key_cast}
                    st.session_state["search_message"] = (
                        "success",
                        "To see the ID's of the search result, click on the button."
                    )

    message = st.session_state.get("search_message")
    if message:
        level, text = message
        if level == "error":
            st.error(text)
        elif level == "success":
            st.success(text)

    results = st.session_state.get("search_results")
    if results:
        selected_id = st.selectbox("Select an incident ID", results["ids"])
        record = data.get(selected_id)
        if record:
            st.json(record)


#  3. MULTI-SEARCH
elif page == "Multi-Search":
    crime_header("Multi-Criteria Search")

    if "multi_results" not in st.session_state:
        st.session_state["multi_results"] = None
    if "multi_message" not in st.session_state:
        st.session_state["multi_message"] = None

    col1, col2 = st.columns(2)

    with col1:
        colA = st.selectbox("Column 1", list(trees.keys()))
        valA = st.text_input("Value for Column 1")
        if colA not in NUMERIC_COLUMNS:
            valA = normalize_text_input(valA)

    with col2:
        colB = st.selectbox("Column 2", list(trees.keys()))
        valB = st.text_input("Value for Column 2")
        if colB not in NUMERIC_COLUMNS:
            valB = normalize_text_input(valB)

    if st.button("Run Multi-Search"):
        valid1, key1, err1 = validate_input(colA, valA)
        valid2, key2, err2 = validate_input(colB, valB)
        if not valid1 or not valid2:
            st.session_state["multi_results"] = None
            st.session_state["multi_message"] = ("error", err1 if not valid1 else err2)
        else:
            result = crime.multisearch(trees, [colA, colB], [key1, key2])
            if isinstance(result, str):
                st.session_state["multi_results"] = None
                st.session_state["multi_message"] = ("error", result)
            else:
                ids = list(result.keys())
                st.session_state["multi_results"] = {"ids": ids, "records": result}
                st.session_state["multi_message"] = (
                    "success",
                    "To see the ID's of the search result, click on the button."
                )

    multi_message = st.session_state.get("multi_message")
    if multi_message:
        lvl, text = multi_message
        if lvl == "error":
            st.error(text)
        elif lvl == "success":
            st.success(text)

    multi_results = st.session_state.get("multi_results")
    if multi_results:
        selected = st.selectbox("Select an incident ID", multi_results["ids"], key="multi_select")
        record = multi_results["records"].get(selected)
        if record:
            st.json(record)


#  4. INSERT RECORD
elif page == "Insert Record":
    crime_header("Insert New Crime Record")

    if "insert_message" not in st.session_state:
        st.session_state["insert_message"] = None
    if "insert_record" not in st.session_state:
        st.session_state["insert_record"] = None

    year = st.number_input("Year", min_value=0, max_value=2050, step=1, value=0)
    v_age = st.number_input("Victim Age", min_value=0, max_value=120, step=1, value=0)
    o_age = st.number_input("Offender Age", min_value=0, max_value=120, step=1, value=0)

    city = st.text_input("City")
    state = st.text_input("State")
    weapon = st.text_input("Weapon Used")
    rel = st.text_input("Relationship")
    cat = st.text_input("Crime Category")

    # Default empty strings to "None" for alphabetic fields
    def default_alpha(value):
        formatted = normalize_text_input(value) if value else ""
        return formatted if formatted else "None"

    city = default_alpha(city)
    state = default_alpha(state)
    weapon = default_alpha(weapon)
    rel = default_alpha(rel)
    cat = default_alpha(cat)

    if st.button("Insert Record"):
        validations = {
            "city": city,
            "state": state,
            "weapon_used": weapon,
            "relationship": rel,
            "crime_category": cat,
        }

        errors = []
        cleaned = {}
        for column, value in validations.items():
            ok, casted, err = validate_input(column, value or "")
            if not ok:
                errors.append(err)
            else:
                cleaned[column] = casted

        if errors:
            st.session_state["insert_record"] = None
            st.session_state["insert_message"] = ("error", errors[0])
        else:
            new_id = crime.insert_record(
                int(year),
                cleaned["city"],
                cleaned["state"],
                int(v_age),
                int(o_age),
                cleaned["weapon_used"],
                cleaned["relationship"],
                cleaned["crime_category"],
            )
            st.session_state["insert_record"] = data.get(new_id)
            st.session_state["insert_message"] = ("success", f"Record inserted with ID {new_id}.")

    insert_msg = st.session_state.get("insert_message")
    if insert_msg:
        lvl, text = insert_msg
        if lvl == "error":
            st.error(text)
        elif lvl == "success":
            st.success(text)

    inserted = st.session_state.get("insert_record")
    if inserted:
        st.json(inserted)


#  5. DELETE RECORD
elif page == "Delete Record":
    crime_header("Delete Crime Record")

    id_to_delete = st.number_input("Incident ID", min_value=1)

    if st.button("Delete"):
        ok = crime.delete_record(int(id_to_delete))
        if ok:
            st.success("Record deleted.")
        else:
            st.error("Record not found.")


#  6. MODIFY RECORD
elif page == "Modify Record":
    crime_header("Modify Crime Record")

    incident_id = st.number_input("Incident ID", min_value=1)

    col = st.selectbox("Column to modify", list(trees.keys()))
    new_val = st.text_input("New value")

    if st.button("Apply Modification"):
        casted = int(new_val) if col in ["year", "victim_age", "offender_age"] else normalize_text_input(new_val)
        updated = crime.modify_record(int(incident_id), **{col: casted})
        if not updated:
            st.error("Incident not found or no changes were applied.")
        else:
            st.success(f"Incident {incident_id} updated.")
            st.json(updated)


#  7. RANGE QUERY
elif page == "Range Query":
    crime_header("Range Query")

    if "range_results" not in st.session_state:
        st.session_state["range_results"] = None
    if "range_message" not in st.session_state:
        st.session_state["range_message"] = None

    col = st.selectbox("Choose column", ["year","city","state","victim_age","offender_age","weapon_used","relationship","crime_category"])
    s = st.text_input("Start value")
    e = st.text_input("End value")
    if col not in NUMERIC_COLUMNS:
        s = normalize_text_input(s)
        e = normalize_text_input(e)

    if st.button("Run Range Query"):
        valid_start, cast_start, err_start = validate_input(col, s)
        valid_end, cast_end, err_end = validate_input(col, e)
        if not valid_start or not valid_end:
            st.session_state["range_results"] = None
            st.session_state["range_message"] = ("error", err_start if not valid_start else err_end)
        else:
            start_val, end_val = cast_start, cast_end
            if start_val > end_val:
                start_val, end_val = end_val, start_val

            results = crime.range_query(col, start_val, end_val)
            if not results:
                st.session_state["range_results"] = None
                st.session_state["range_message"] = ("error", "No incidents found in that range.")
            else:
                if isinstance(results, list):
                    records = {rid: data.get(rid) for rid in results if rid in data}
                elif isinstance(results, dict):
                    records = results
                else:
                    records = {}
                st.session_state["range_results"] = records
                st.session_state["range_message"] = (
                    "success",
                    f"Found {len(records)} incidents for {col} between {start_val} and {end_val}."
                )

    range_message = st.session_state.get("range_message")
    if range_message:
        lvl, text = range_message
        if lvl == "error":
            st.error(text)
        elif lvl == "success":
            st.success(text)

    range_results = st.session_state.get("range_results")
    if range_results:
        sorted_ids = sorted(range_results.keys())
        selected_range_id = st.selectbox("Select an incident ID", sorted_ids, key="range_select")
        record = range_results.get(selected_range_id)
        if record:
            st.json(record)


#  8. GRAPH ALGORITHMS
elif page == "Graph Algorithms":
    crime_header("Graph Algorithms on Crime States")

    state_graph = crime.get_city_graph()
    if not state_graph:
        st.info("Graph data is empty. Insert incidents to build connections.")
    else:
        st.markdown("### Compare Two States")
        states = sorted(state_graph.keys())
        col_left, col_right = st.columns(2)
        with col_left:
            state_a = st.selectbox("State A", states, key="state_a_select")
        with col_right:
            state_b = st.selectbox("State B", states, key="state_b_select")

        if state_a == state_b:
            st.warning("Please choose two different states to compare.")
        else:
            relations = state_graph.get(state_a, {}).get(state_b)
            if not relations:
                st.info(f"No shared crime/weapon combos between {state_a} and {state_b}.")
            else:
                st.json({f"{state_a} ↔ {state_b}": relations})

    g = crime.graph()
    if not g.graph:
        st.warning("No edges available for running graph algorithms.")
    else:
        start_nodes = sorted(g.graph.keys())
        start = st.selectbox("Start node for traversals", start_nodes)

        st.subheader("DFS")
        st.write(crime.dfs(g, start))

        st.subheader("BFS (distance by hops)")
        st.write(crime.bfs(g, start))

        st.subheader("Bellman-Ford Distances")
        dist, _ = crime.bellman_ford(g, start)
        st.write(dist)


#  9. STATISTICS
elif page == "Statistics":
    crime_header("Data Statistics")

    col = st.selectbox("Column", ["victim_age", "offender_age", "year"])

    st.metric("Min", crime.compute_min(data, col))
    st.metric("Max", crime.compute_max(data, col))
    st.metric("Average", crime.compute_average(data, col))
    st.metric("Median", crime.compute_median(data, col))

    st.subheader("Most Common Entries")
    st.write(crime.top_k_frequent(data, col))


# =====================
#  10. KNN
# =====================
elif page == "KNN Similarity":
    crime_header("KNN Similarity Search")

    query = st.number_input("Incident ID", 1)

    features = ["victim_age", "offender_age", "year"]

    K = st.number_input("K", 1, 50)

    if st.button("Find Similar Records"):
        neighbors = crime.knn(data, int(query), features, int(K))
        if not neighbors:
            st.error("Incident not found or not enough data for comparison.")
        else:
            for entry in neighbors:
                st.write(f"Incident {entry['incident_id']} (distance {entry['distance']:.2f})")
                st.json(entry["record"])
