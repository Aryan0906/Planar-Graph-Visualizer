import streamlit as st
import networkx as nx
import json
import matplotlib.pyplot as plt
import os
    
    # Function to check planarity and calculate Euler's formula
def check_planarity_and_euler(edges):
        graph = nx.Graph()
        graph.add_edges_from(edges)
        is_planar, embedding = nx.check_planarity(graph)
        if is_planar:
            V = graph.number_of_nodes()
            E = graph.number_of_edges()
            F = E - V + 2  # Euler's formula for planar graphs
            return is_planar, V, E, F, graph
        else:
            return is_planar, None, None, None, graph
    
    # Function to save the graph visualization
def save_graph_image(graph, filename="graph.png"):
        plt.figure(figsize=(8, 6))
        nx.draw(graph, with_labels=True, node_color="lightblue", edge_color="gray", node_size=500, font_size=10)
        plt.savefig(filename)
        plt.close()
    
    # Streamlit App
def main():
        # App title and header
        st.markdown(
            """
            <div style="background-color:#007bff;padding:10px;border-radius:10px">
                <h1 style="color:white;text-align:center;">Planar Graph Visualizer</h1>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
        # Sidebar for navigation
        st.sidebar.title("Navigation")
        options = st.sidebar.radio("Go to", ["Home", "About Planar Graphs", "Contact Us"])
    
        if options == "Home":
            # Description
            st.write(
                """
                A **planar graph** is a graph that can be drawn on a plane without any edges crossing.
                Use this tool to check if your graph is planar and visualize it.
                """
            )
    
            # Input for graph edges
            st.subheader("Enter Graph Data")
            edges_input = st.text_area(
                "Graph Edges (JSON Format)",
                placeholder='[{"source": "A", "target": "B"}, {"source": "B", "target": "C"}, {"source": "C", "target": "D"}]',
                help="Enter the edges of the graph in JSON format. Each edge should have a 'source' and 'target'.",
            )
    
            # Buttons
            col1, col2 = st.columns(2)
            with col1:
                check_button = st.button("Check Planarity")
            with col2:
                reset_button = st.button("Reset Input")
    
            if reset_button:
                st.experimental_rerun()
    
            if check_button:
                try:
                    # Parse edges input
                    edges = json.loads(edges_input)
                    edges_list = [(edge["source"], edge["target"]) for edge in edges]
    
                    # Check planarity and calculate Euler's formula
                    is_planar, V, E, F, graph = check_planarity_and_euler(edges_list)
    
                    if is_planar:
                        st.success("The graph is planar.")
                        st.write(f"**Vertices (V):** {V}")
                        st.write(f"**Edges (E):** {E}")
                        st.write(f"**Faces (F):** {F}")
    
                        # Save and display the graph visualization
                        save_graph_image(graph)
                        st.image("graph.png", caption="Graph Visualization")
    
                        # Download button for the graph image
                        with open("graph.png", "rb") as file:
                            btn = st.download_button(
                                label="Download Graph Visualization",
                                data=file,
                                file_name="graph.png",
                                mime="image/png",
                            )
                    else:
                        st.warning("The graph is NOT planar.")
                except json.JSONDecodeError:
                    st.error("Invalid JSON format. Please check your input.")
                except Exception as e:
                    st.error(f"Error: {e}")
    
        elif options == "About Planar Graphs":
            # About Planar Graphs Section
            st.subheader("What is a Planar Graph?")
            st.write(
                """
                A **planar graph** is a graph that can be drawn on a plane such that no edges intersect except at their endpoints.
                """
            )
            st.write("### Examples:")
            col1, col2 = st.columns(2)
            with col1:
                st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Planar_graph_example.svg/512px-Planar_graph_example.svg.png", caption="Planar Graph", use_column_width=True)
            with col2:
                st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/K5_graph.svg/512px-K5_graph.svg.png", caption="Non-Planar Graph (K5)", use_column_width=True)
    
            st.write(
                """
                ### Euler's Formula:
                For a connected planar graph:
                \[
                V - E + F = 2
                \]
                Where:
                - \(V\): Number of vertices
                - \(E\): Number of edges
                - \(F\): Number of faces
                """
            )
    
        elif options == "Contact Us":
            # Contact Us Section
            st.subheader("Contact Us")
            st.write("For any questions or feedback, please reach out:")
            st.write("- **Email**: support@planargraph.com")
            st.write("- **GitHub**: [Planar Graph Visualizer](https://github.com/your-repo)")
            st.write("- **Twitter**: [@PlanarGraph](https://twitter.com/PlanarGraph)")
    
        # Footer
        st.markdown(
            """
            <hr>
            <div style="text-align:center;">
                <p>Developed with ❤️ using Streamlit</p>
                <p><a href="https://github.com/your-repo" target="_blank">GitHub Repository</a></p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
if __name__ == "__main__":
        main()