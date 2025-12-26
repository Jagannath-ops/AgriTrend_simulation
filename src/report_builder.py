from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.enums import TA_CENTER
from pathlib import Path


def build_pdf_report():
    """
    Builds the final PDF report for AgriTrend Simulation.
    """

    # --------------------------------------------------
    # Paths
    # --------------------------------------------------
    output_pdf = Path("outputs/reports/universal_data.pdf")

    graph_yield = Path("outputs/graphs/yield_trend.png")
    graph_standardized = Path("outputs/graphs/standardized_trends.png")

    output_pdf.parent.mkdir(parents=True, exist_ok=True)

    # --------------------------------------------------
    # Document setup
    # --------------------------------------------------
    doc = SimpleDocTemplate(
        str(output_pdf),
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    styles = getSampleStyleSheet()
    story = []

    # --------------------------------------------------
    # PAGE 1 — COVER
    # --------------------------------------------------

    title_style = ParagraphStyle(
        name="TitleStyle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=22,
        spaceAfter=20,
    )

    subtitle_style = ParagraphStyle(
        name="SubtitleStyle",
        parent=styles["Normal"],
        alignment=TA_CENTER,
        fontSize=11,
        textColor="grey",
        spaceAfter=30,
    )

    story.append(Paragraph("AgriTrend_simulation", title_style))

    story.append(
        Paragraph(
            "A research-oriented simulation framework for studying crop yield "
            "dynamics through synthetic environmental data",
            subtitle_style,
        )
    )

    story.append(Spacer(1, 30))

    story.append(Paragraph("<b>Abstract</b>", styles["Heading2"]))
    story.append(Spacer(1, 10))

    abstract_text = """
    Agriculture today is under increasing pressure from climate change, soil degradation,
    and growing demand. Yields no longer improve simply by adding more inputs, and in many
    regions they are becoming unstable or slowly declining. This raises a serious concern:
    are we approaching limits that traditional farming practices cannot overcome?
    <br/><br/>
    AgriTrend_simulation explores this problem using a controlled, research-oriented
    simulation framework. Instead of aiming for exact prediction, the system focuses on
    understanding long-term trends, sensitivities, and trade-offs between environmental
    factors and management decisions.
    <br/><br/>
    The results show a difficult reality — long-term stress dominates agricultural systems.
    However, the analysis also reveals that coordinated, sustained improvements can meaningfully
    slow or partially reverse negative trends. The future is challenging, but it is not fixed.
    """

    story.append(Paragraph(abstract_text, styles["Normal"]))

    story.append(PageBreak())

    # --------------------------------------------------
    # PAGE 2 — SYSTEM OVERVIEW
    # --------------------------------------------------

    story.append(Paragraph("System Overview", styles["Heading1"]))
    story.append(Spacer(1, 12))

    overview_text = """
    AgriTrend_simulation is designed to answer one simple question:
    <br/><br/>
    <i>“If current trends continue, what happens to crop yield — and what changes actually matter?”</i>
    <br/><br/>
    To keep the system understandable and transparent, it follows three guiding principles:
    <br/><br/>
    • The system avoids black-box models and uses explainable statistical relationships.<br/>
    • The focus is on long-term behavior rather than short-term prediction accuracy.<br/>
    • Every step is modular, so real datasets can replace synthetic data without redesign.
    <br/><br/>
    At a high level, the system works as follows:
    <br/><br/>
    Synthetic environmental and management data is generated to reflect realistic agricultural
    behavior. Historical trends are analyzed to understand how different factors move together.
    A regression model learns how yield responds to these factors. The model is then used to
    project a baseline future and compare it against controlled improvement scenarios.
    <br/><br/>
    This structure allows users to quickly grasp what drives yield decline, what helps,
    and what does not — without needing to read or understand the underlying code.
    """

    story.append(Paragraph(overview_text, styles["Normal"]))

    story.append(PageBreak())

    # --------------------------------------------------
    # PAGE 3 — SYNTHETIC DATA & HISTORICAL REALITY
    # --------------------------------------------------

    story.append(Paragraph("Synthetic Data and Historical Reality", styles["Heading1"]))
    story.append(Spacer(1, 12))

    synthetic_text = """
    Real, clean, long-term agricultural datasets are often difficult to obtain.
    To overcome this, the system uses synthetically generated data that is statistically
    realistic and grounded in known agricultural behavior.
    <br/><br/>
    The synthetic dataset includes rainfall, temperature, soil quality, irrigation coverage,
    fertilizer usage, pest pressure, and resulting crop yield. Each variable follows
    realistic constraints, trends, and variability observed in real-world systems.
    <br/><br/>
    This approach allows the system to study relationships and long-term dynamics without
    relying on any single region or crop. The same architecture can later be applied
    directly to real tabular datasets.
    """

    story.append(Paragraph(synthetic_text, styles["Normal"]))
    story.append(Spacer(1, 20))

    if graph_yield.exists():
        story.append(Paragraph("<b>Historical Yield Trend</b>", styles["Heading3"]))
        story.append(Spacer(1, 10))
        img = Image(str(graph_yield), width=450, height=220)
        story.append(img)

    story.append(PageBreak())

    # --------------------------------------------------
    # PAGE 4 — RELATIVE TRENDS
    # --------------------------------------------------

    story.append(Paragraph("Relative Trends Across Factors", styles["Heading1"]))
    story.append(Spacer(1, 12))

    trend_text = """
    Different agricultural factors operate on very different scales.
    To compare them meaningfully, all variables are standardized relative
    to their historical behavior.
    <br/><br/>
    This visualization highlights an important pattern: while management inputs
    such as irrigation and fertilizer steadily increase, crop yield does not follow
    the same trajectory. Instead, yield diverges downward over time.
    <br/><br/>
    This gap signals diminishing system efficiency — a warning that input
    intensification alone is not enough to sustain long-term productivity.
    """

    story.append(Paragraph(trend_text, styles["Normal"]))
    story.append(Spacer(1, 20))

    if graph_standardized.exists():
        img = Image(str(graph_standardized), width=450, height=220)
        story.append(img)

    # --------------------------------------------------
    # BUILD PDF
    # --------------------------------------------------

        story.append(PageBreak())

    # --------------------------------------------------
    # PAGE 5 — BASELINE FUTURE
    # --------------------------------------------------

    story.append(Paragraph("Baseline Future: If Nothing Changes", styles["Heading1"]))
    story.append(Spacer(1, 12))

    baseline_text = """
    The baseline future represents a continuation of current trends.
    It assumes no new technologies, no major policy shifts, and no
    additional effort beyond what is already happening today.
    <br/><br/>
    Rainfall follows long-term climate drift, temperature continues
    to rise slowly, soil quality degrades gradually, and management
    inputs such as irrigation and fertilizer grow only through
    existing infrastructure expansion.
    <br/><br/>
    Under these conditions, crop yield becomes increasingly unstable
    and shows a general downward trend. Some years perform reasonably
    well, but poor years become more frequent and more severe.
    <br/><br/>
    This baseline is not pessimistic — it is simply what the system
    predicts if we continue on the current path without coordinated
    intervention.
    """

    story.append(Paragraph(baseline_text, styles["Normal"]))

    story.append(PageBreak())

    # --------------------------------------------------
    # PAGE 6 — BEST-CASE 1% IMPROVEMENT SCENARIO
    # --------------------------------------------------

    story.append(Paragraph("Best-Case Scenario: Coordinated 1% Improvements", styles["Heading1"]))
    story.append(Spacer(1, 12))

    scenario_text = """
    To explore whether decline is inevitable, the system evaluates
    a best-case scenario based on small but sustained improvements.
    <br/><br/>
    In this scenario, multiple factors improve together every year:
    rainfall effectiveness increases, temperature stress is slightly
    reduced, soil health improves, irrigation coverage expands, and
    fertilizer use becomes more effective.
    <br/><br/>
    Each change is modest — just one percent per year — but applied
    consistently over time.
    <br/><br/>
    The results show that while such improvements do not create a
    dramatic surge in yield, they significantly slow decline and
    lead to a more stable and higher yield trajectory compared to
    the baseline future.
    <br/><br/>
    This suggests that the agricultural system is stressed, but not
    irreversibly broken. Coordinated action matters.
    """

    story.append(Paragraph(scenario_text, styles["Normal"]))
    story.append(Spacer(1, 20))

    scenario_graph = Path("outputs/graphs/baseline_vs_best_case.png")

    if scenario_graph.exists():
        img = Image(str(scenario_graph), width=450, height=220)
        story.append(img)

    story.append(PageBreak())

    # --------------------------------------------------
    # PAGE 7 — CONCLUSIONS & LIMITATIONS
    # --------------------------------------------------

    story.append(Paragraph("Conclusions and Limitations", styles["Heading1"]))
    story.append(Spacer(1, 12))

    conclusion_text = """
    This simulation highlights a difficult but realistic picture of
    modern agriculture. Long-term environmental stress and system
    degradation play a larger role in yield outcomes than individual
    management inputs.
    <br/><br/>
    Simply adding more fertilizer or expanding irrigation is not
    enough to reverse long-term decline. However, the analysis also
    shows that coordinated, sustained improvements across multiple
    factors can meaningfully change the future.
    <br/><br/>
    It is important to recognize the limits of this system. The model
    is linear, does not capture complex feedback loops, and relies on
    synthetic data rather than real field observations. Its strength
    lies in understanding trends and sensitivities, not exact
    prediction.
    <br/><br/>
    Future work will focus on integrating real datasets, expanding
    scenario exploration, and providing interactive interfaces that
    allow users to explore outcomes dynamically.
    """

    story.append(Paragraph(conclusion_text, styles["Normal"]))

    doc.build(story)
