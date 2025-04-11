This My collage project Discirt Mathematics and Graph Theory 
Planar Graph Visualizer is a dynamic Streamlit application for exploring planar graphs: check planarity, compute Euler’s formula, and interactively visualize graph structures in real time.

It’s organized into five main sections—Home, Edit Graph, Live Graph, Learn, and Contact—each designed to guide you through understanding and working with graph planarity:

1. **Home**  
   • Introduces planar graphs and their importance.  
   • Provides quick examples (triangle, square, K₅) that you can paste in JSON format to check planarity.  
   • Uses Lottie animations for a modern, engaging interface.

2. **Edit Graph**  
   • A form-driven editor where you define nodes (comma‑separated) and edges (one per line as A‑B).  
   • Renders your custom graph with Plotly’s interactive layout.  
   • Displays planarity status, vertex/edge/face counts, and offers export options (JSON download, copy to clipboard).

3. **Live Graph**  
   • Pre‑built examples (K₃, C₄, K₅, K₃,₃) with interactive tabs.  
   • Each example shows the graph, its metrics, and an explanation of why it’s planar or not.

4. **Learn**  
   • Educational content on planar graph theory: definitions, Euler’s formula, Kuratowski’s theorem, and real‑world applications.  
   • Embedded images and charts to illustrate concepts.

5. **Contact**  
   • A simple form for feedback, bug reports, or collaboration requests.  
   • FAQ section addressing common questions about planar graphs and the tool’s capabilities.

**Key Technical Details**  
• **Backend & Graph Logic:** Uses NetworkX to test planarity and compute Euler’s formula (V – E + F = 2).  
• **Visualization:** Generates interactive, zoomable graphs with Plotly (via `st.plotly_chart`).  
• **UI Framework:** Streamlit widgets (`st.radio`, `st.button`, `st.text_area`) and custom CSS for responsiveness.  
• **Animations:** Integrates Lottie JSON animations for dynamic visual feedback.  
• **Run Command:** Launch the app locally with  
  `streamlit run dmgt.py`  

This tool bridges theoretical graph concepts and hands‑on exploration, making planar graph analysis accessible and visually engaging.
