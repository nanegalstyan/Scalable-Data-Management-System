
import numpy as np
import pandas as pd
import random
#from faker import Faker
from ds_collection import AVLTreeMap
import csv
from collections import defaultdict, deque



data = {}
with open("crime_reports_fast.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["year"] = int(row["year"])
        row["incident_id"] = int(row["incident_id"])
        row["victim_age"] = int(row["victim_age"])
        row["offender_age"] = int(row["offender_age"])
        idd = row["incident_id"]
        data[idd] = row
data


class ColumnsAVL(AVLTreeMap):
    def put(self, k, v):
        self._check_key(k)
        p = self._subtree_search(self._tree.root(), k)

        if self._tree.is_external(p):
            # Key not found: expand external and rebalance
            self._expand_external(p, self._MapEntry(k, [int(v)]))
            self._rebalance_insert(p)
            return None
        else:
            # Add new value to the same key
            value = p.get_element().get_value()
            value.append(int(v))
            return None

    def remove(self, k, v):
        if self.is_empty():
            return None

        p = self._subtree_search(self._tree.root(), k)
        if self._tree.is_external(p):
            # Key not found
            return None

        old_value = p.get_element().get_value()
        if len(old_value) == 1:

            # Case: two internal children → replace with in-order predecessor
            if self._tree.is_internal(self._tree.left(p)) and self._tree.is_internal(self._tree.right(p)):
                replacement = self._tree_max(self._tree.left(p))
                self._tree.set(p, replacement.get_element())
                p = replacement

            # Now p has at most one internal child
            child_sentinel = self._tree.left(p) if self._tree.is_external(self._tree.left(p)) else self._tree.right(p)
            sibling = self._tree.sibling(child_sentinel)

            self._tree.remove(child_sentinel)
            self._tree.remove(p)
            self._rebalance_delete(sibling)

            return old_value[0]
        else:
            value = p.get_element().get_value()
            value.remove(v)
            return v
        

class AdjacencyMapGraph:
    def __init__(self, directed=True):
        self.directed = directed
        self.graph = {}  # {u: {v: weight}}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = {}

    def add_edge(self, u, v, w=1):
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u][v] = w
        if not self.directed:
            self.graph[v][u] = w

    def vertices(self):
        return list(self.graph.keys())

    def edges(self):
        e = []
        for u in self.graph:
            for v, w in self.graph[u].items():
                e.append((u, v, w))
        return e

    def neighbors(self, v):
        return list(self.graph[v].keys())

from collections import defaultdict

def build_city_similarity_graph(data):
    combo_counts = defaultdict(lambda: defaultdict(int))
    graph = AdjacencyMapGraph(directed=False)

    for rec in data.values():
        state = rec["state"]
        category = rec["crime_category"]
        weapon = rec["weapon_used"]
        combo_counts[(category, weapon)][state] += 1

    for (category, weapon), state_freq in combo_counts.items():
        states = list(state_freq.keys())
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                state_a, state_b = states[i], states[j]
                weight = max(state_freq[state_a], state_freq[state_b])
                current = graph.graph.get(state_a, {}).get(state_b, 0)
                graph.add_edge(state_a, state_b, current + weight)

    return graph

_city_graph_display = {}
_graph_instance = AdjacencyMapGraph(directed=False)


def _compute_graph_structures(records):
    combo_counts = defaultdict(lambda: defaultdict(int))
    for rec in records.values():
        state = rec["state"]
        category = rec["crime_category"]
        weapon = rec["weapon_used"]
        combo_counts[(category, weapon)][state] += 1

    display = defaultdict(lambda: defaultdict(list))
    graph_obj = AdjacencyMapGraph(directed=False)

    for (category, weapon), state_freq in combo_counts.items():
        states = list(state_freq.keys())
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                state_a, state_b = states[i], states[j]
                weight = state_freq[state_a] + state_freq[state_b]
                display[state_a][state_b].append(
                    {"crime": category, "weapon": weapon, "weight": weight}
                )
                display[state_b][state_a].append(
                    {"crime": category, "weapon": weapon, "weight": weight}
                )
                current = graph_obj.graph.get(state_a, {}).get(state_b, 0)
                graph_obj.add_edge(state_a, state_b, current + weight)

    normalized = {state: dict(neighbors) for state, neighbors in display.items()}
    return normalized, graph_obj


def _rebuild_graph_structures():
    global _city_graph_display, _graph_instance
    _city_graph_display, _graph_instance = _compute_graph_structures(data)


year_column = ColumnsAVL()
for incident_id, row in data.items():
    year_column.put(row["year"], incident_id)


city_column = ColumnsAVL()
for incident_id, row in data.items():
    city_column.put(row["city"], incident_id)


state_column = ColumnsAVL()
for incident_id, row in data.items():
    state_column.put(row["state"], incident_id)

victim_age = ColumnsAVL()
for incident_id, row in data.items():
    victim_age.put(row["victim_age"], incident_id)


offender_age = ColumnsAVL()
for incident_id, row in data.items():
    offender_age.put(row["offender_age"], incident_id)

weapon_used = ColumnsAVL()
for incident_id, row in data.items():
    weapon_used.put(row["weapon_used"], incident_id)


relationship_column = ColumnsAVL()
for incident_id, row in data.items():
    relationship_column.put(row["relationship"], incident_id)


crime_category_column = ColumnsAVL()
for incident_id, row in data.items():
    crime_category_column.put(row["crime_category"], incident_id)


root = crime_category_column._tree._root.get_element()
print(type(crime_category_column._tree._root.get_element()))
print(root)


trees = {"year": year_column, "city": city_column, "state": state_column, "victim_age": victim_age,
         "offender_age": offender_age, "weapon_used": weapon_used, "relationship": relationship_column,
          "crime_category": crime_category_column}

_rebuild_graph_structures()


def search(trees, column, key, incident_id=None):
    tree = trees[column]
    values = tree.get(key)
    if not values:
        return [], None

    record = None
    if incident_id is not None and incident_id in values:
        record = data.get(incident_id)

    return values, record

def multisearch(trees, columns, keys):
    candidate_sets = []
    for column, key in zip(columns, keys):
        tree = trees[column]
        values = tree.get(key)
        if not values:
            return f"There are no such incidents where the {column} is {key}."
        candidate_sets.append(set(values))

    commons = set.intersection(*candidate_sets) if candidate_sets else set()
    if not commons:
        return "There are no such incidents where the given criteria satisfy."

    results = {incident_id: data[incident_id] for incident_id in sorted(commons)}
    return results

NUMERIC_RANGE_COLUMNS = {"year", "victim_age", "offender_age"}


def range_query(column, start, end):
    tree = trees[column]
    results = {}

    if column in NUMERIC_RANGE_COLUMNS:
        start_val = int(start)
        end_val = int(end)
        upper_bound = end_val + 1
    else:
        start_val = str(start)
        end_val = str(end)
        upper_bound = end_val

    if start_val > end_val:
        start_val, end_val = end_val, start_val
        if column in NUMERIC_RANGE_COLUMNS:
            upper_bound = end_val + 1
        else:
            upper_bound = end_val

    seen_keys = set()
    for entry in tree.sub_map(start_val, upper_bound):
        key = entry.get_key()
        seen_keys.add(key)
        for incident_id in entry.get_value():
            record = data.get(incident_id)
            if record:
                results[incident_id] = record

    if column not in NUMERIC_RANGE_COLUMNS and end_val not in seen_keys:
        ids = tree.get(end_val)
        if ids:
            for incident_id in ids:
                record = data.get(incident_id)
                if record:
                    results[incident_id] = record

    return results


def delete_record(incident_id: int, csv_path: str = "crime_reports_fast.csv") -> bool:
    global data, trees

    incident = data.get(incident_id)
    if not incident:
        print(f"Incident {incident_id} not found.")
        return False

    fieldnames_template = list(incident.keys())

    def remove_from_index(index, key, id_value):
        ids = index.get(key)
        if ids is None:
            return
        index.remove(key, id_value)

    for column, value in incident.items():
        if column in trees:
            remove_from_index(trees[column], value, incident_id)

    data.pop(incident_id)
    _rebuild_graph_structures()

    if csv_path:
        if data:
            fieldnames = list(next(iter(data.values())).keys())
        else:
            fieldnames = fieldnames_template
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data.values())

    print(f"Incident {incident_id} successfully deleted and saved to {csv_path}.")
    return True


def insert_record(year="None", city="None", state="None", victim_age=0, offender_age=0, weapon_used="None", relationship="None", crime_category="None", csv_path="crime_reports_fast.csv"):
    global data, trees
    new_id = max(data.keys()) + 1
    data[new_id] = {
        "incident_id": new_id,
        "year": year,
        "city": city,
        "state": state,
        "victim_age": victim_age,
        "offender_age": offender_age,
        "weapon_used": weapon_used,
        "relationship": relationship,
        "crime_category": crime_category
    }

    for key, value in data[new_id].items():
        if key in trees:
            trees[key].put(value, new_id)

    if csv_path:
        fieldnames = ["incident_id", "year", "city", "state", "victim_age", "offender_age", "weapon_used", "relationship", "crime_category"]
        with open(csv_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if f.tell() == 0:
                writer.writeheader()
            writer.writerow(data[new_id])

    _rebuild_graph_structures()
    return new_id


def modify_record(incident_id, csv_path="crime_reports_fast.csv", **fields):
    global trees, data

    record = data.get(incident_id)
    if record is None:
        print(f"Incident {incident_id} not found.")
        return None

    updated_keys = []
    for key, val in fields.items():
        if key not in record:
            continue
        old = record[key]
        if old == val:
            continue
        record[key] = val
        if key in trees:
            tree = trees[key]
            tree.remove(old, incident_id)
            tree.put(val, incident_id)
        updated_keys.append(key)

    if not updated_keys:
        return record

    if csv_path:
        fieldnames = ["incident_id", "year", "city", "state", "victim_age", "offender_age", "weapon_used", "relationship", "crime_category"]
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for incident in sorted(data.values(), key=lambda row: row["incident_id"]):
                writer.writerow(incident)

    _rebuild_graph_structures()
    return record


def get_city_graph():
    return _city_graph_display


def graph(metric="sum"):
    return _graph_instance


def dfs(graph, start):
    visited = set()
    order = []

    def explore(v):
        visited.add(v)
        order.append(v)
        for nbr in graph.graph[v]:
            if nbr not in visited:
                explore(nbr)

    explore(start)
    return order


def bfs(graph, start):
    visited = set([start])
    dist = {start: 0}
    queue = deque([start])

    while queue:
        u = queue.popleft()
        for v in graph.graph[u]:
            if v not in visited:
                visited.add(v)
                dist[v] = dist[u] + 1
                queue.append(v)

    return dist


def bellman_ford(graph, source):
    dist = {v: float("inf") for v in graph.graph}
    parent = {v: None for v in graph.graph}
    dist[source] = 0

    # Build edge list
    edges = []
    for u in graph.graph:
        for v, w in graph.graph[u].items():
            edges.append((u, v, w))

    V = len(graph.graph)

    # Relax edges V-1 times
    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u

    # Detect negative cycles
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            print("Negative cycle detected!")

    return dist, parent




import statistics

def get_column_values(data, col):
    values = []
    for rec in data.values():
        if col in rec and rec[col] != "" and rec[col] is not None:
            try:
                values.append(float(rec[col]))
            except:
                pass
    return values


def compute_min(data, col):
    values = get_column_values(data, col)
    return min(values) if values else None

def compute_max(data, col):
    values = get_column_values(data, col)
    return max(values) if values else None

def compute_average(data, col):
    values = get_column_values(data, col)
    return sum(values) / len(values) if values else None

def compute_median(data, col):
    values = get_column_values(data, col)
    return statistics.median(values) if values else None

from collections import Counter

def top_k_frequent(data, col, K=10):
    counter = Counter()

    for rec in data.values():
        if col in rec:
            counter[rec[col]] += 1

    return counter.most_common(K)


def top_k_by_value(data, col, K=10):
    records = []

    for rec in data.values():
        if col in rec:
            try:
                records.append((rec[col], rec))
            except:
                pass

    # Sort by numeric value descending
    records.sort(key=lambda x: float(x[0]), reverse=True)
    return records[:K]


#KNN
def record_to_vector(rec, features):
    vec = []
    for f in features:
        try:
            vec.append(float(rec[f]))
        except:
            vec.append(0.0)
    return vec


import math

def euclidean(v1, v2):
    return math.sqrt(sum((a - b)**2 for a, b in zip(v1, v2)))



def knn(data, query_id, features, K=5):
    target = data.get(query_id)
    if target is None:
        return []

    target_vec = record_to_vector(target, features)
    distances = []
    for rid, rec in data.items():
        if rid == query_id:
            continue
        vec = record_to_vector(rec, features)
        dist = euclidean(target_vec, vec)
        distances.append((dist, rid, rec))

    distances.sort(key=lambda x: x[0])
    top = []
    for dist, rid, rec in distances[:K]:
        top.append({
            "incident_id": rid,
            "distance": dist,
            "record": rec,
        })
    return top
