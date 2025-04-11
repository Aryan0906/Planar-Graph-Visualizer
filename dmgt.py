import streamlit as st
import networkx as nx
import json
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
import requests
from datetime import datetime


# Function to load Lottie animations
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Check planarity and Euler's formula
def check_planarity_and_euler(edges):
    """
    Function to check if a graph is planar and calculate Euler's formula components.
    """
    graph = nx.Graph()
    graph.add_edges_from(edges)
    is_planar, embedding = nx.check_planarity(graph)
    if is_planar:
        V = graph.number_of_nodes()
        E = graph.number_of_edges()
        F = E - V + 2  # Euler's formula for planar graphs
        return is_planar, V, E, F, graph
    return is_planar, None, None, None, graph


# Interactive Plotly graph
def plot_interactive_graph(graph):
    """
    Function to create an interactive graph visualization using Plotly.
    """
    pos = nx.spring_layout(graph, seed=42)
    edge_x, edge_y = [], []
    for edge in graph.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=2, color="#4287f5"),
        hoverinfo='none',
        mode='lines')

    node_x, node_y, text = [], [], []
    for node in graph.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        text.append(str(node))

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        hoverinfo='text',
        marker=dict(
            showscale=False,
            color="#1f77b4",
            size=30,
            line=dict(width=2, color="#ffffff")),
        text=text,
        textposition="top center"
    )

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        paper_bgcolor="#f8f9fa",
                        plot_bgcolor="#f8f9fa",
                        font=dict(color="#60B5FF", family="Outfit"),
                        title=dict(
                            text='Interactive Graph View',
                            font=dict(size=22, family="Outfit", color="#60B5FF")
                        ),
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=60),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )
    return fig


# Streamlit App
st.set_page_config(page_title="Planar Graph Visualizer", layout="wide", page_icon="🧠")

st.markdown("""
    <div style='background: linear-gradient(90deg, #123458 0%, #1a4b7c 100%); 
         padding: 1rem; 
         border-radius: 10px; 
         margin-bottom: 2rem;
         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
        <div style='display: flex; align-items: center; justify-content: center;'>
            <h1 style='color: white; 
                      font-size: 2.5rem; 
                      margin: 0;
                      padding: 1rem;
                      text-align: center;
                      font-weight: 600;
                      letter-spacing: 1px;'>
                🔰 Planar Graph Visualizer
            </h1>
        </div>
        <div style='text-align: center;
                    padding-top: 0.5rem;
                    border-top: 1px solid rgba(255, 255, 255, 0.1);
                    margin-top: 0.5rem;'>
            <span style='color: #e0e0e0; 
                       font-size: 1rem;'>
                Visualize • Analyze • Learn
            </span>
        </div>
    </div>
""", unsafe_allow_html=True)
# Custom CSS
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        .nav-container {
            max-width: 800px;
            margin: 2rem auto;
            padding: 0.5rem;
            background: linear-gradient(135deg, #123458 0%, #2C5282 100%);
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        
        .nav-items {
            display: flex;
            justify-content: center;
            gap: 1rem;
            padding: 0.5rem;
        }
        
        .nav-button {
            background: rgba(255, 255, 255, 0.1);
            border: none;
            padding: 1rem;
            color: white;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: center;
            min-width: 100px;
        }
        
        .nav-button:hover {
            background: rgba(255, 255, 255, 0.2);
            transform: translateY(-2px);
        }
        
        .nav-button.active {
            background: white;
            color: #123458;
        }
        
        .nav-icon {
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
            display: block;
        }
        
        .nav-text {
            font-size: 0.9rem;
            font-weight: 500;
        }
        
        @media (max-width: 768px) {
            .nav-items {
                flex-wrap: wrap;
            }
            
            .nav-button {
                flex: 1 1 calc(33.333% - 1rem);
                min-width: 80px;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Navigation Bar
page = st.radio(
    "Navigation",
    ["🏠 Home", "📐 Edit Graph", "📊 Live Graph", "📚 Learn", "📬 Contact"], 
    horizontal=True, 
)

# Page Logic
if page == "🏠 Home":
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        <div class='card'>
            <h2>🔍 What is a Planar Graph?</h2>
            <p style='font-size:1.1rem; line-height:1.6;'>
                A planar graph can be drawn on a 2D surface without any edge crossings. 
                This property is fundamental in various fields including circuit design, 
                map coloring, and network visualization.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='card'>
            <h3>✏ Try It Yourself</h3>
            <p>Paste your graph below in JSON format to check if it's planar!</p>
        </div>
        """, unsafe_allow_html=True)

        graph_input = st.text_area("",
                                   placeholder='[{"source": "A", "target": "B"}, {"source": "B", "target": "C"}, {"source": "C", "target": "A"}]',
                                   height=150, label_visibility="collapsed")

        check_button = st.button("Check Planarity", use_container_width=True)

    with col2:
        # Add a lottie animation for the home page
        lottie_url = "https://assets9.lottiefiles.com/packages/lf20_kkflmtur.json"  # Graph animation
        lottie_json = load_lottie_url(lottie_url)
        if lottie_json:
            st_lottie(lottie_json, height=300, key="home_animation")

        st.markdown("""
        <div class='card'>
            <h4>Quick Examples</h4>
            <ul>
                <li>Triangle: <code>[["A", "B"], ["B", "C"], ["C", "A"]]</code></li>
                <li>Square: <code>[["A", "B"], ["B", "C"], ["C", "D"], ["D", "A"]]</code></li>
                <li>K5 (Non-planar): <code>[["1", "2"], ["1", "3"], ["1", "4"], ["1", "5"], ["2", "3"], ["2", "4"], ["2", "5"], ["3", "4"], ["3", "5"], ["4", "5"]]</code></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    if check_button and graph_input:
        try:
            edges = json.loads(graph_input)

            # Handle both formats: list of dictionaries or list of lists
            if isinstance(edges[0], dict):
                edge_list = [(e["source"], e["target"]) for e in edges]  # Format: [{"source": "A", "target": "B"}]
            elif isinstance(edges[0], list):
                edge_list = edges  # Format: [[1, 2], [2, 3]]
            else:
                raise ValueError("Invalid edge format. Use a list of dictionaries or a list of lists.")

            is_planar, V, E, F, G = check_planarity_and_euler(edge_list)

            st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)

            if is_planar:
                st.markdown("""
                <div style='background-color:#e6f7e6; border-left:4px solid #28a745; padding:1rem; border-radius:0.5rem; margin-bottom:1.5rem;'>
                    <h3 style='color:#28a745; margin:0;'>✅ The graph is planar!</h3>
                </div>
                """, unsafe_allow_html=True)

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown(f"""
                    <div class='metric-card'>
                        <div class='metric-value'>{V}</div>
                        <div class='metric-label'>Vertices</div>
                    </div>
                    """, unsafe_allow_html=True)

                with col2:
                    st.markdown(f"""
                    <div class='metric-card'>
                        <div class='metric-value'>{E}</div>
                        <div class='metric-label'>Edges</div>
                    </div>
                    """, unsafe_allow_html=True)

                with col3:
                    st.markdown(f"""
                    <div class='metric-card'>
                        <div class='metric-value'>{F}</div>
                        <div class='metric-label'>Faces</div>
                    </div>
                    """, unsafe_allow_html=True)

                st.markdown("<div style='height:1rem;'></div>", unsafe_allow_html=True)
                st.plotly_chart(plot_interactive_graph(G), use_container_width=True)

                st.info("💡 Euler's formula V - E + F = 2 is satisfied for this planar graph.")

            else:
                st.markdown("""
                <div style='background-color:#fff4e6; border-left:4px solid #fd7e14; padding:1rem; border-radius:0.5rem; margin-bottom:1.5rem;'>
                    <h3 style='color:#fd7e14; margin:0;'>❌ The graph is NOT planar.</h3>
                    <p style='margin-top:0.5rem;'>This graph cannot be drawn on a plane without edge crossings.</p>
                </div>
                """, unsafe_allow_html=True)

                st.plotly_chart(plot_interactive_graph(G), use_container_width=True)

                st.info(
                    "💡 Non-planar graphs like K5 (complete graph with 5 vertices) and K3,3 (utility graph) cannot be drawn without edge crossings.")

        except Exception as e:
            st.error(f"Error: {e}")
            st.markdown("""
            <div style='background-color:#f8d7da; padding:1rem; border-radius:0.5rem;'>
                <p>Please check your input format. Examples:</p>
                <ul>
                    <li><code>[["A", "B"], ["B", "C"], ["C", "A"]]</code></li>
                    <li><code>[{"source": "A", "target": "B"}, {"source": "B", "target": "C"}]</code></li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

elif page == "📐 Edit Graph":
    st.markdown("""
    <div class='card'>
        <h2>✏ Node & Edge Editor</h2>
        <p>Create your own graph by defining nodes and edges below.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        with st.form("graph_editor"):
            st.markdown("<h4>Define Your Graph</h4>", unsafe_allow_html=True)
            node_names = st.text_input("Nodes (comma separated)", value="A,B,C,D")
            edge_pairs = st.text_area("Edges (each as A-B)", value="A-B\nB-C\nC-D\nD-A", height=150)
            submitted = st.form_submit_button("Render Graph", use_container_width=True)

    with col2:
        st.markdown("""
        <div class='card'>
            <h4>Tips for Creating Graphs</h4>
            <ul>
                <li>Use simple labels for nodes (A, B, 1, 2, etc.)</li>
                <li>Each edge should connect two existing nodes</li>
                <li>For a planar graph, avoid creating too many crossing edges</li>
                <li>Try creating classic structures like cycles, trees, or grids</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        # Add a small lottie animation
        lottie_url = "https://assets3.lottiefiles.com/packages/lf20_ystsffqy.json"  # Edit animation
        lottie_json = load_lottie_url(lottie_url)
        if lottie_json:
            st_lottie(lottie_json, height=180, key="edit_animation")

    if submitted:
        try:
            nodes = [n.strip() for n in node_names.split(",") if n.strip()]
            edges = [(e.split("-")[0].strip(), e.split("-")[1].strip()) for e in edge_pairs.strip().split("\n") if
                     "-" in e]

            G = nx.Graph()
            G.add_nodes_from(nodes)
            G.add_edges_from(edges)

            is_planar, V, E, F, _ = check_planarity_and_euler(edges)

            st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)

            st.markdown("""
            <div class='card'>
                <h3>Your Graph Visualization</h3>
            </div>
            """, unsafe_allow_html=True)

            st.plotly_chart(plot_interactive_graph(G), use_container_width=True)

            if is_planar:
                st.markdown(f"""
                <div style='background-color:#e6f7e6; border-left:4px solid #28a745; padding:1rem; border-radius:0.5rem;'>
                    <h4 style='color:#28a745; margin:0;'>✅ This is a planar graph!</h4>
                    <p style='margin-top:0.5rem;'>Vertices: {V} | Edges: {E} | Faces: {F}</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div style='background-color:#fff4e6; border-left:4px solid #fd7e14; padding:1rem; border-radius:0.5rem;'>
                    <h4 style='color:#fd7e14; margin:0;'>❌ This graph is NOT planar.</h4>
                </div>
                """, unsafe_allow_html=True)

            # Add export options
            st.markdown("<div style='height:1rem;'></div>", unsafe_allow_html=True)
            export_col1, export_col2 = st.columns(2)

            with export_col1:
                edge_list_json = json.dumps([{"source": e[0], "target": e[1]} for e in edges])
                st.download_button(
                    label="📥 Export as JSON",
                    data=edge_list_json,
                    file_name="graph_data.json",
                    mime="application/json",
                )

            with export_col2:
                st.button("📋 Copy to Clipboard", key="copy_btn")

        except Exception as e:
            st.error(f"Error: {e}")
            st.markdown("""
            <div style='background-color:#f8d7da; padding:1rem; border-radius:0.5rem;'>
                <p>Please check your input format:</p>
                <ul>
                    <li>Nodes should be comma-separated (e.g., A,B,C,D)</li>
                    <li>Edges should be in the format A-B, one per line</li>
                    <li>Make sure all edge endpoints exist in your node list</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

elif page == "📊 Live Graph":
    st.markdown("""
    <div class='card'>
        <h2>📈 Interactive Graph Examples</h2>
        <p>Explore these pre-built graph examples to understand planar and non-planar structures.</p>
    </div>
    """, unsafe_allow_html=True)

    example_tabs = st.tabs(["Triangle (K3)", "Square (C4)", "Complete Graph (K5)", "Utility Graph (K3,3)", "Custom"])

    with example_tabs[0]:
        st.markdown("<h4>Triangle (K3) - Planar</h4>", unsafe_allow_html=True)
        triangle_edges = [("A", "B"), ("B", "C"), ("C", "A")]
        _, V, E, F, G = check_planarity_and_euler(triangle_edges)

        col1, col2 = st.columns([3, 1])
        with col1:
            st.plotly_chart(plot_interactive_graph(G), use_container_width=True)
        with col2:
            st.markdown(f"""
            <div class='metric-card' style='background-color:#123458; color:white; padding:1rem; border-radius:0.5rem; text-align:center;'>
                <div class='metric-value' style='font-size:2rem; font-weight:700; color:white;'>{V}</div>
                <div class='metric-label' style='font-size:0.9rem; color:white; margin-top:0.3rem;'>Vertices</div>
            </div>
            <div style='height:0.5rem;'></div>
            <div class='metric-card' style='background-color:#123458; color:white; padding:1rem; border-radius:0.5rem; text-align:center;'>
                <div class='metric-value' style='font-size:2rem; font-weight:700; color:white;'>{E}</div>
                <div class='metric-label' style='font-size:0.9rem; color:white; margin-top:0.3rem;'>Edges</div>
            </div>
            <div style='height:0.5rem;'></div>
            <div class='metric-card' style='background-color:#123458; color:white; padding:1rem; border-radius:0.5rem; text-align:center;'>
                <div class='metric-value' style='font-size:2rem; font-weight:700; color:white;'>{F}</div>
                <div class='metric-label' style='font-size:0.9rem; color:white; margin-top:0.3rem;'>Faces</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style='margin-top:1rem;'>
                <code>[["A", "B"], ["B", "C"], ["C", "A"]]</code>
            </div>
            """, unsafe_allow_html=True)

    with example_tabs[1]:
        st.markdown("<h4>Square (C4) - Planar</h4>", unsafe_allow_html=True)
        square_edges = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")]
        _, V, E, F, G = check_planarity_and_euler(square_edges)

        col1, col2 = st.columns([3, 1])
        with col1:
            st.plotly_chart(plot_interactive_graph(G), use_container_width=True)
        with col2:
            st.markdown(f"""
            <div class='metric-card' style='background-color:#123458; color:white; padding:1rem; border-radius:0.5rem; text-align:center;'>
                <div class='metric-value' style='font-size:2rem; font-weight:700; color:white;'>{V}</div>
                <div class='metric-label' style='font-size:0.9rem; color:white; margin-top:0.3rem;'>Vertices</div>
            </div>
            <div style='height:0.5rem;'></div>
            <div class='metric-card' style='background-color:#123458; color:white; padding:1rem; border-radius:0.5rem; text-align:center;'>
                <div class='metric-value' style='font-size:2rem; font-weight:700; color:white;'>{E}</div>
                <div class='metric-label' style='font-size:0.9rem; color:white; margin-top:0.3rem;'>Edges</div>
            </div>
            <div style='height:0.5rem;'></div>
            <div class='metric-card' style='background-color:#123458; color:white; padding:1rem; border-radius:0.5rem; text-align:center;'>
                <div class='metric-value' style='font-size:2rem; font-weight:700; color:white;'>{F}</div>
                <div class='metric-label' style='font-size:0.9rem; color:white; margin-top:0.3rem;'>Faces</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style='margin-top:1rem;'>
                <code>[["A", "B"], ["B", "C"], ["C", "D"], ["D", "A"]]</code>
            </div>
            """, unsafe_allow_html=True)

    with example_tabs[2]:
        st.markdown("<h4>Complete Graph (K5) - Non-Planar</h4>", unsafe_allow_html=True)
        k5_edges = [("1", "2"), ("1", "3"), ("1", "4"), ("1", "5"),
                    ("2", "3"), ("2", "4"), ("2", "5"),
                    ("3", "4"), ("3", "5"),
                    ("4", "5")]
        is_planar, _, _, _, G = check_planarity_and_euler(k5_edges)

        col1, col2 = st.columns([3, 1])
        with col1:
            st.plotly_chart(plot_interactive_graph(G), use_container_width=True)
        with col2:
            st.markdown("""
            <div style='background-color:#fff4e6; border-left:4px solid #fd7e14; padding:1rem; border-radius:0.5rem;'>
                <h4 style='color:#fd7e14; margin:0;'>Non-Planar Graph</h4>
                <p>K5 is one of the Kuratowski graphs that cannot be drawn on a plane without edge crossings.</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style='margin-top:1rem;'>
                <p>Complete graph with 5 vertices where every vertex is connected to all others.</p>
            </div>
            """, unsafe_allow_html=True)

    with example_tabs[3]:
        st.markdown("<h4>Utility Graph (K3,3) - Non-Planar</h4>", unsafe_allow_html=True)
        k33_edges = [("A", "1"), ("A", "2"), ("A", "3"),
                     ("B", "1"), ("B", "2"), ("B", "3"),
                     ("C", "1"), ("C", "2"), ("C", "3")]
        is_planar, _, _, _, G = check_planarity_and_euler(k33_edges)

        col1, col2 = st.columns([3, 1])
        with col1:
            st.plotly_chart(plot_interactive_graph(G), use_container_width=True)
        with col2:
            st.markdown("""
            <div style='background-color:#fff4e6; border-left:4px solid #fd7e14; padding:1rem; border-radius:0.5rem;'>
                <h4 style='color:#fd7e14; margin:0;'>Non-Planar Graph</h4>
                <p>K3,3 is the other Kuratowski graph that cannot be drawn on a plane without edge crossings.</p>
            </div>
            """"", unsafe_allow_html=True)
            st.markdown("""
            <div style='margin-top:1rem;'>
                <p>Also known as the "Utility Graph" - represents 3 houses connected to 3 utilities.</p>
            </div>
            """, unsafe_allow_html=True)

    with example_tabs[4]:
        st.markdown("<h4>Custom Graph</h4>", unsafe_allow_html=True)

        custom_nodes = st.text_input("Nodes (comma separated)", value="A,B,C,D,E")
        custom_edges = st.text_area("Edges (each as A-B)", value="A-B\nB-C\nC-D\nD-E\nE-A", height=150)

        if st.button("Generate Custom Graph", use_container_width=True):
            try:
                nodes = [n.strip() for n in custom_nodes.split(",") if n.strip()]
                edges = [(e.split("-")[0].strip(), e.split("-")[1].strip()) for e in custom_edges.strip().split("\n") if
                         "-" in e]

                G = nx.Graph()
                G.add_nodes_from(nodes)
                G.add_edges_from(edges)

                is_planar, V, E, F, _ = check_planarity_and_euler(edges)

                st.plotly_chart(plot_interactive_graph(G), use_container_width=True)

                if is_planar:
                    st.markdown(f"""
                    <div style='background-color:#e6f7e6; border-left:4px solid #28a745; padding:1rem; border-radius:0.5rem;'>
                        <h4 style='color:#28a745; margin:0;'>✅ This is a planar graph!</h4>
                        <p style='margin-top:0.5rem;'>Vertices: {V} | Edges: {E} | Faces: {F}</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div style='background-color:#fff4e6; border-left:4px solid #fd7e14; padding:1rem; border-radius:0.5rem;'>
                        <h4 style='color:#fd7e14; margin:0;'>❌ This graph is NOT planar.</h4>
                    </div>
                    """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")

elif page == "📚 Learn":
    st.markdown("""
    <div class='card'>
        <h2>📚 Learn About Planar Graphs</h2>
        <p>Explore the fascinating world of planar graphs and their applications.</p>
    </div>
    """, unsafe_allow_html=True)

    learn_tabs = st.tabs(["Basics", "Euler's Formula", "Kuratowski's Theorem", "Applications", "Resources"])

    with learn_tabs[0]:
        col1, col2 = st.columns([3, 2])

        with col1:
            st.markdown("""
            <h3>What is a Planar Graph?</h3>
            <p>A graph is called <b>planar</b> if it can be drawn on a plane (or a sphere) in such a way that no edges cross each other. In other words, it can be drawn so that no edges intersect except at their endpoints (vertices).</p>

            <h4>Key Properties:</h4>
            <ul>
                <li>Every planar graph can be drawn with straight-line edges</li>
                <li>A planar graph with n ≥ 3 vertices has at most 3n - 6 edges</li>
                <li>A planar graph always has a vertex with degree at most 5</li>
                <li>Every planar graph is 4-colorable (Four Color Theorem)</li>
            </ul>
            """, unsafe_allow_html=True)

        with col2:
            # Add a lottie animation for the learn page
            lottie_url = "https://assets5.lottiefiles.com/packages/lf20_qp1q7mct.json"  # Education animation
            lottie_json = load_lottie_url(lottie_url)
            if lottie_json:
                st_lottie(lottie_json, height=250, key="learn_animation")

            st.markdown("""
            <div style='background-color:#e6f7ff; border-left:4px solid #1890ff; padding:1rem; border-radius:0.5rem; margin-top:1rem;'>
                <h4 style='color:#1890ff; margin:0;'>Did You Know?</h4>
                <p>The study of planar graphs began with the famous "Seven Bridges of Königsberg" problem, solved by Leonhard Euler in 1736.</p>
            </div>
            """, unsafe_allow_html=True)

    with learn_tabs[1]:
        st.markdown("""
        <h3>Euler's Formula</h3>
        <p>For any connected planar graph with V vertices, E edges, and F faces (including the outer face), Euler's formula states:</p>
        <div style='text-align:center; font-size:1.5rem; margin:1.5rem 0; font-weight:bold; color:#123458;'>
            V - E + F = 2
        </div>

        <h4>Example:</h4>
        <p>Consider a cube drawn in the plane:</p>
        <ul>
            <li>Vertices (V): 8</li>
            <li>Edges (E): 12</li>
            <li>Faces (F): 6</li>
        </ul>
        <p>Applying Euler's formula: 8 - 12 + 6 = 2 ✓</p>

        <h4>Consequences of Euler's Formula:</h4>
        <ul>
            <li>For a simple planar graph with n ≥ 3 vertices: E ≤ 3n - 6</li>
            <li>For a simple bipartite planar graph: E ≤ 2n - 4</li>
            <li>Every planar graph has a vertex of degree at most 5</li>
        </ul>
        """, unsafe_allow_html=True)

        # Add a simple visualization
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Schlegel_wireframe_8-cell.png/440px-Schlegel_wireframe_8-cell.png",
            caption="A planar embedding of a cube", width=300)

    with learn_tabs[2]:
        st.markdown("""
        <h3>Kuratowski's Theorem</h3>
        <p>Kuratowski's theorem provides a complete characterization of planar graphs:</p>
        <div style='background-color:#f0f2f5; padding:1rem; border-radius:0.5rem; margin:1rem 0;'>
            <p style='font-weight:bold;'>A graph is planar if and only if it does not contain a subgraph that is a subdivision of K₅ or K₃,₃.</p>
        </div>

        <h4>The Forbidden Subgraphs:</h4>
        <ul>
            <li><b>K₅</b>: The complete graph on 5 vertices</li>
            <li><b>K₃,₃</b>: The complete bipartite graph with 3 vertices in each part (also known as the "utility graph")</li>
        </ul>

        <p>A <b>subdivision</b> of a graph is obtained by replacing edges with paths. This means that if you can find either K₅ or K₃,₃ within your graph (possibly with some edges replaced by paths), then your graph is not planar.</p>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<h5 style='text-align:center;'>K₅ (Complete Graph)</h5>", unsafe_allow_html=True)
            k5_edges = [("1", "2"), ("1", "3"), ("1", "4"), ("1", "5"),
                        ("2", "3"), ("2", "4"), ("2", "5"),
                        ("3", "4"), ("3", "5"),
                        ("4", "5")]
            G_k5 = nx.Graph()
            G_k5.add_edges_from(k5_edges)
            st.plotly_chart(plot_interactive_graph(G_k5), use_container_width=True)

        with col2:
            st.markdown("<h5 style='text-align:center;'>K₃,₃ (Utility Graph)</h5>", unsafe_allow_html=True)
            k33_edges = [("A", "1"), ("A", "2"), ("A", "3"),
                         ("B", "1"), ("B", "2"), ("B", "3"),
                         ("C", "1"), ("C", "2"), ("C", "3")]
            G_k33 = nx.Graph()
            G_k33.add_edges_from(k33_edges)
            st.plotly_chart(plot_interactive_graph(G_k33), use_container_width=True)

    with learn_tabs[3]:
        st.markdown("""
        <h3>Applications of Planar Graphs</h3>
        <p>Planar graphs have numerous practical applications across various fields:</p>
        """, unsafe_allow_html=True)

        app_col1, app_col2 = st.columns(2)

        with app_col1:
            st.markdown("""
            <div style='background-color:#f0f8ff; padding:1rem; border-radius:0.5rem; height:100%;'>
                <h4 style='color:#123458;'>Circuit Design</h4>
                <p>Planar graphs are essential in designing printed circuit boards (PCBs) where crossing wires can cause short circuits.</p>
                <h4 style='color:#123458;'>Map Coloring</h4>
                <p>The Four Color Theorem states that any planar graph can be colored with at most four colors, which has applications in map coloring problems.</p>
                <h4 style='color:#123458;'>Network Design</h4>
                <p>Planning road networks, utility distribution, and telecommunication networks often involves planar graph considerations.</p>
            </div>
            """, unsafe_allow_html=True)

        with app_col2:
            st.markdown("""
            <div style='background-color:#f0f8ff; padding:1rem; border-radius:0.5rem; height:100%;'>
                <h4 style='color:#123458;'>VLSI Design</h4>
                <p>Very Large Scale Integration (VLSI) chip design relies on planar graph algorithms to minimize wire crossings.</p>
                <h4 style='color:#123458;'>Graph Drawing</h4>
                <p>Visualizing complex networks in a clear, readable manner often involves planar graph drawing algorithms.</p>
                <h4 style='color:#123458;'>Computational Geometry</h4>
                <p>Triangulations, Voronoi diagrams, and other geometric structures are closely related to planar graphs.</p>
            </div>
            """, unsafe_allow_html=True)

    with learn_tabs[4]:
        st.markdown("""
        <h3>Learning Resources</h3>
        <p>Explore these resources to deepen your understanding of planar graphs:</p>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style='background-color:#f5f5f5; padding:1.5rem; border-radius:0.5rem;'>
            <h4>Books</h4>
            <ul>
                <li>"Graph Theory" by Reinhard Diestel</li>
                <li>"Introduction to Graph Theory" by Douglas B. West</li>
                <li>"Planar Graphs: Theory and Algorithms" by Takao Nishizeki and Norishige Chiba</li>
            </ul>

            <h4>Online Courses</h4>
            <ul>
                <li>Coursera: "Discrete Mathematics" by University of California San Diego</li>
                <li>edX: "Graph Theory" by University of California San Diego</li>
                <li>Khan Academy: "Graph Theory Basics"</li>
            </ul>

            <h4>Interactive Tools</h4>
            <ul>
                <li><a href="https://d3gt.com/unit.html" target="_blank">D3 Graph Theory</a> - Interactive graph theory tutorials</li>
                <li><a href="https://graphonline.ru/en/" target="_blank">Graph Online</a> - Create and analyze graphs</li>
                <li><a href="https://www.geogebra.org/m/nbjfjtpv" target="_blank">GeoGebra: Graph Theory</a> - Interactive graph theory demonstrations</li>
            </ul>

            <h4>Research Papers</h4>
            <ul>
                <li>"Planarity Testing in Parallel" by J. Hopcroft and R. Tarjan</li>
                <li>"Linear-Time Algorithms for Testing the Planarity of Graphs" by N. Chiba et al.</li>
                <li>"Efficient Algorithms for Maximum Planar Subgraphs" by C. Gutwenger and P. Mutzel</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

elif page == "📬 Contact":
    st.markdown("""
    <div class='card'>
        <h2>📬 Contact Us</h2>
        <p>Have questions, feedback, or suggestions? We'd love to hear from you!</p>
    </div>
    """, unsafe_allow_html=True)

    contact_col1, contact_col2 = st.columns([3, 2])

    with contact_col1:
        st.markdown("<h3>Send us a message</h3>", unsafe_allow_html=True)

        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            subject = st.selectbox("Subject",
                                   ["General Inquiry", "Bug Report", "Feature Request", "Collaboration", "Other"])
            message = st.text_area("Message", height=150)
            submitted = st.form_submit_button("Send Message", use_container_width=True)

            if submitted:
                st.success("Thank you for your message! We'll get back to you soon.")
                # Here you would typically add code to send the message via email or save to a database

    with contact_col2:
        st.markdown("""
        <div style='background-color:#AFDDFF; padding:1.5rem; border-radius:0.5rem;'>
            <h4>Get in Touch</h4>
            <p>Reach out with questions, feedback, or collaboration:</p>


        <p>📧 <b>Email:</b><a href="#"> support@planargraph.com</a></p>
        <p>🧠 <b>GitHub:</b> <a href="https://github.com/your-repo" target="_blank">Graph Master</a></p>
        <p>🐦 <b>Twitter:</b> <a href="https://twitter.com/PlanarGraph" target="_blank">@PlanarGraph</a></p>

        </div>
        """, unsafe_allow_html=True)

        # Add a lottie animation for the contact page
        lottie_url = "https://assets9.lottiefiles.com/packages/lf20_in4cufsz.json"  # Message/contact animation
        lottie_json = load_lottie_url(lottie_url)
        if lottie_json:
            st_lottie(lottie_json, height=200, key="contact_animation")

    st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)

    st.markdown("""
    <h3>Frequently Asked Questions</h3>
    """, unsafe_allow_html=True)

    with st.expander("What is a planar graph?"):
        st.markdown("""
        A planar graph is a graph that can be drawn on a plane without any edges crossing. 
        In other words, it can be drawn so that no edges intersect except at their endpoints (vertices).
        """)

    with st.expander("How can I determine if my graph is planar?"):
        st.markdown("""
        You can use our tool to check if your graph is planar! Simply input your graph's edges in the 
        format shown in the examples, and our algorithm will determine if it's planar. 

        Alternatively, you can use Kuratowski's theorem, which states that a graph is planar if and only if 
        it doesn't contain a subdivision of K₅ or K₃,₃.
        """)

    with st.expander("Can I export my graph visualization?"):
        st.markdown("""
        Yes! After creating your graph in the "Edit Graph" section, you'll see options to export your graph 
        as JSON or copy the data to your clipboard. You can also take a screenshot of the visualization.
        """)

    with st.expander("Are there any limitations to the tool?"):
        st.markdown("""
        The current version has some limitations:

        - Very large graphs (hundreds of nodes) may have slower performance
        - The automatic layout algorithm may not always produce the most visually pleasing arrangement
        - Custom styling options are limited in the current version

        We're continuously improving the tool and welcome your feedback!
        """)


def home():
    st.title("ðŸ§  Planar Graph Visualizer")

    # Hero section
    st.markdown("""
    <div style='background-color:#123458; padding:2rem; border-radius:10px; margin-bottom:2rem;'>
        <h2 style='color:white; text-align:center;'>Explore, Create, and Analyze Planar Graphs</h2>
        <p style='color:#e0e0e0; text-align:center; font-size:1.2rem;'>
            A powerful tool for visualizing and understanding graph planarity
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Features section
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style='background-color:#f8f9fa; padding:1.5rem; border-radius:10px; height:100%; text-align:center;'>
            <h3 style='color:#123458;'>âœ Create</h3>
            <p>Build custom graphs with an intuitive interface. Add nodes and edges with ease.</p>
            <p><a href="?page=edit" style='color:#123458; font-weight:bold;'>Try the Editor â†’</a></p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='background-color:#f8f9fa; padding:1.5rem; border-radius:10px; height:100%; text-align:center;'>
            <h3 style='color:#123458;'>🔍 Analyze</h3>
            <p>Check if your graph is planar and visualize it with interactive controls.</p>
            <p><a href="?page=analyze" style='color:#123458; font-weight:bold;'>Analyze a Graph →</a></p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style='background-color:#f8f9fa; padding:1.5rem; border-radius:10px; height:100%; text-align:center;'>
            <h3 style='color:#123458;'>📚 Learn</h3>
            <p>Explore the theory behind planar graphs and their applications.</p>
            <p><a href="?page=learn" style='color:#123458; font-weight:bold;'>Start Learning →</a></p>
        </div>
        """, unsafe_allow_html=True)

    # Quick start section
    st.markdown("""
    <h2 style='margin-top:3rem; text-align:center;'>Quick Start</h2>
    <p style='text-align:center; margin-bottom:2rem;'>Try our tool with these simple examples</p>
    """, unsafe_allow_html=True)

    quick_col1, quick_col2 = st.columns([3, 2])

    with quick_col1:
        st.markdown("<h4>Check if your graph is planar:</h4>", unsafe_allow_html=True)

        example_input = st.text_area(
            "Enter edges as pairs (one per line):",
            "A-B\nB-C\nC-D\nD-A\nA-C",
            height=150
        )

        if st.button("Check Planarity", use_container_width=True):
            try:
                edges = [(e.split("-")[0].strip(), e.split("-")[1].strip()) for e in example_input.strip().split("\n")
                         if "-" in e]

                G = nx.Graph()
                G.add_edges_from(edges)

                is_planar, V, E, F, _ = check_planarity_and_euler(edges)

                st.plotly_chart(plot_interactive_graph(G), use_container_width=True)

                if is_planar:
                    st.success(f"✅ This graph is planar! Vertices: {V}, Edges: {E}, Faces: {F}")
                else:
                    st.warning("❌ This graph is NOT planar.")
            except Exception as e:
                st.error(f"Error: {e}")

    with quick_col2:
        st.markdown("<h4>Try these examples:</h4>", unsafe_allow_html=True)

        st.markdown("""
        <div style='background-color:#f0f8ff; padding:1rem; border-radius:0.5rem; margin-bottom:1rem;'>
            <h5 style='margin-top:0;'>Triangle (Planar)</h5>
            <code>A-B<br>B-C<br>C-A</code>
        </div>

        <div style='background-color:#f0f8ff; padding:1rem; border-radius:0.5rem; margin-bottom:1rem;'>
            <h5 style='margin-top:0;'>Square with Diagonal (Planar)</h5>
            <code>A-B<br>B-C<br>C-D<br>D-A<br>A-C</code>
        </div>

        <div style='background-color:#fff4e6; padding:1rem; border-radius:0.5rem;'>
            <h5 style='margin-top:0;'>K5 (Non-Planar)</h5>
            <code>1-2<br>1-3<br>1-4<br>1-5<br>2-3<br>2-4<br>2-5<br>3-4<br>3-5<br>4-5</code>
        </div>
        """, unsafe_allow_html=True)


# Footer
st.markdown("""
    <div style="text-align: center; margin-top: 2rem; font-size: 0.9rem; color: #666;">
        <hr>
        <p>© 2025 Planar Graph Visualizer. All rights reserved.</p>
    </div>
""", unsafe_allow_html=True)
