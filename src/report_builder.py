from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Image,PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.enums import TA_CENTER
from pathlib import Path
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors


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
        rightMargin=50,
        leftMargin=50,
        topMargin=40,
        bottomMargin=40,
    )

    styles = getSampleStyleSheet()
    story = []

# --------------------------------------------------
# PAGE 1 START
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
        fontSize=13,
        textColor="grey",
        spaceAfter=20,
    )

    story.append(Paragraph("AgriTrend_simulation", title_style))

    story.append(
        Paragraph(
            "A research-oriented simulation framework to study crop yield trends using synthetic environmental data",
            subtitle_style,
        )
    )

    story.append(Spacer(1, 10))
    
    abstract_text = '''
    <para align="center">
    <b>Abstract</b>
    <br/><br/>

    <i>
    Agriculture today is under growing pressure from climate change,
    soil degradation, and rising food demand.
    </i>
    <br/><br/>

    In many regions, crop yields are no longer improving in a stable way.
    Adding more fertilizer or irrigation does not always lead to better results,
    and in some cases yields slowly decline over time.
    <br/><br/>

    <b>
    This raises a critical question:
    </b>
    <br/>
    <i>
    Are current farming practices reaching their limits under long-term environmental stress?
    </i>
    <br/><br/>

    <b>AgriTrend_simulation</b> is designed to explore this problem through a
    research-oriented and transparent simulation framework.
    Instead of predicting exact future yields, the system focuses on
    understanding long-term trends and how different factors interact.
    <br/><br/>

    The simulation uses synthetic but realistic data to model rainfall,
    temperature, soil health, irrigation, fertilizer use, pest pressure,
    and their combined effect on crop yield.
    A baseline future is projected assuming no major changes, and this is
    compared against scenarios with small, coordinated improvements.
    <br/><br/>

    The results point to a difficult reality :
    <b>Long-term system stress dominates agricultural outcomes.</b>
    <br/><br/>
    However, they also reveal something important.
    <br/><br/>
    <i>
    Decline is not inevitable.
    </i>
    <br/><br/>

    Even modest, sustained improvements when applied together
    can slow negative trends and create a more stable future.
    <br/><br/>

    <b>
    The future is challenging, but it is not fixed.
    </b>
    </para>
    '''
    abstract_style = ParagraphStyle(
        name="AbstractStyle",
        parent=styles["Normal"],
        alignment=TA_CENTER,
        fontSize=13,          
        leading=18,           
        spaceAfter=20,
    )
    
    story.append(Paragraph(abstract_text, abstract_style))


# --------------------------------------------------
# PAGE 1 END
# --------------------------------------------------

    story.append(PageBreak())

# --------------------------------------------------
# PAGE 2 START
# --------------------------------------------------

    story.append(Paragraph("System Overview", styles["Heading1"]))
    story.append(Spacer(1, 14))

    overview_text = '''
    <b>What is this system trying to do?</b>
    <br/><br/>

    AgriTrend_simulation is built to understand one core idea:
    <br/>
    <i>
    If farming continues the way it is today, what happens to crop yield in the future (10 years from now)?
    </i>
    <br/><br/>

    Instead of focusing on short-term predictions, the system looks at
    <b>long-term trends</b> and looks which factors matter most over time.
    <br/><br/>

    <hr/>

    <b>How the system works :</b>
    <br/><br/>

    <b>1. Synthetic data generation</b>
    <br/>
    The system first creates realistic agricultural data.
    This includes rainfall, temperature, soil quality, irrigation,
    fertilizer use, pest pressure, and crop yield.
    <br/><br/>
        The data is not random noise. Each factor follows:
        <br/>
        • realistic value ranges<br/>
        • slow long-term trends<br/>
        • natural year-to-year variation
    <br/><br/>

    <b>2. Historical trend analysis</b>
    <br/>
    Once the data is created, the system analyzes how each factor
    changes over time and how it relates to yield.
    <br/><br/>
    This helps answer questions like:
    <br/>
    • Is yield improving or declining?<br/>
    • Are inputs increasing faster than output?<br/>
    • Do some factors move together?
    <br/><br/>

    <b>3. Yield response modeling</b>
    <br/>
    A linear regression model is trained using historical data.
    The goal is understanding
    <i>how strongly each factor affects yield</i>.
    <br/><br/>
    Both raw and standardized models are used so that:
    <br/>
    • real-world impact can be measured<br/>
    • relative importance of factors can be compared
    <br/><br/>

    <b>4. Baseline future projection</b>
    <br/>
    Using the trained model, the system projects a future where
    current trends continue with no major intervention.
    <br/><br/>
    This baseline future acts as a reference point and answers:
    <br/>
    <i>What happens if nothing changes?</i>
    <br/><br/>

    <b>5. Controlled improvement scenarios</b>
    <br/>
    Finally, the system applies small, sustained improvements
    to multiple factors at the same time.
    <br/><br/>
    These scenarios test whether coordinated action
    even at just 1% improvement per year
    can meaningfully change long-term outcomes.
    <br/><br/>

    <hr/>

    <b>Why this structure matters</b>
    <br/><br/>

    This step-by-step structure keeps the system simple, transparent, and easy to understand.
    Each module does one clear task, which makes it easy to replace synthetic data with
    real-world datasets in the future without changing the overall design.
    <br/><br/>

    Because of this structure, the system clearly shows what drives long-term yield decline,
    what factors help stabilize agricultural output, and why even small, sustained changes
    can matter when applied over many years.
    '''

    story.append(Paragraph(overview_text, styles["Normal"]))

# --------------------------------------------------
# PAGE 2 END
# --------------------------------------------------

    story.append(PageBreak())

# --------------------------------------------------
# PAGE 3 START
# --------------------------------------------------

    story.append(Paragraph("Synthetic Data Characteristics", styles["Heading1"]))
    story.append(Spacer(1, 10))

    intro_text = '''
    The system uses synthetically generated data that follows realistic agricultural
    behavior, with all variables staying within practical limits and changing
    gradually over time to reflect real environmental and management constraints.
    '''

    story.append(Paragraph(intro_text, styles["Normal"]))

    story.append(Paragraph("<b>Key Assumptions Used in Synthetic Data</b>", styles["Heading3"]))
    story.append(Spacer(1, 3))

    assumption_table = Table(
        [
            ["Factor", "Typical Assumption / Range"],
            ["Rainfall", "~800 mm/year with variability"],
            ["Temperature", "~25 °C average"],
            ["Soil Quality Index", "0.5 - 0.85"],
            ["Irrigation Coverage", "30% /- 70%"],
            ["Fertilizer Usage", "50 - 200 kg/ha"],
            ["Pest Pressure", "0.0 - 1.0 (index)"],
        ],
        colWidths=[200, 300],
    )

    assumption_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONT", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (0, 0), (-1, 0), "CENTER"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))

    story.append(assumption_table)
    story.append(Spacer(1, 12))

    factor_images = [
        "factor_rainfall_mm.png",
        "factor_temperature_c.png",
        "factor_soil_index.png",
        "factor_irrigation_pct.png",
        "factor_fertilizer_kg_ha.png",
        "factor_pest_pressure_index.png",
    ]

    image_cells = []
    row = []

    for i, img_name in enumerate(factor_images):
        img_path = Path("outputs/graphs") / img_name

        if img_path.exists():
            img = Image(str(img_path), width=240, height=140)
        else:
            img = Paragraph("Missing Image", styles["Normal"])

        row.append(img)

        if len(row) == 2:
            image_cells.append(row)
            row = []

    image_grid = Table(
        image_cells,
        colWidths=[260, 260]
    )

    image_grid.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))

    story.append(image_grid)

# --------------------------------------------------
# PAGE 3 START
# --------------------------------------------------

    story.append(PageBreak())

# --------------------------------------------------
# PAGE 4 START
# --------------------------------------------------

    story.append(Paragraph("Historical Reality", styles["Heading1"]))
    story.append(Spacer(1, 12))

    synthetic_text = '''
    The graph below shows how crop yield changes over time when all agricultural
    factors interact together. 
    
    <br/><br/>
    Yield here is not driven by a single variable, but
    by the combined effect of rainfall, temperature, soil health, irrigation,
    fertilizer use, and pest pressure.
    <br/><br/>

    This graph should be read as a system-level signal rather than a year-by-year
    scorecard. Individual years may perform well or poorly, but the long-term
    pattern is what matters most.
    <br/><br/>

    <b>
    Key observations from the yield trend:
    </b>
    <br/>
    • yield does not increase smoothly over time<br/>
    • variability grows as years progress<br/>
    • good years become less predictable<br/>
    • poor years become more frequent
    <br/><br/>

    Even though management inputs such as irrigation and fertilizer increase over
    time, yield does not follow the same upward path. This indicates that rising
    inputs are increasingly used to compensate for environmental stress rather
    than to generate real growth.
    <br/><br/>

    Another important signal is instability. 
    <br/><br/>

    As the system becomes stressed, yield fluctuates more sharply from year to year. This instability is often
    more damaging than slow decline, as it increases risk for farmers and food
    systems.
    <br/><br/>

    This historical yield trend sets the foundation for the rest of the analysis.
    It highlights why simply continuing current practices may not be enough,
    and why future scenarios must be compared against this baseline behavior.
    '''

    story.append(Paragraph(synthetic_text, styles["Normal"]))
    story.append(Spacer(1, 30))

    if graph_yield.exists():
        story.append(Paragraph("<b>Historical Yield Trend</b>", styles["Heading3"]))
        story.append(Spacer(1, 20))
        img = Image(str(graph_yield), width=450, height=220)
        story.append(img)

# --------------------------------------------------
# PAGE 4 END
# --------------------------------------------------

    story.append(PageBreak())

# --------------------------------------------------
# PAGE 5 START
# --------------------------------------------------

    story.append(Paragraph("Relative Trends Across Factors", styles["Heading1"]))
    story.append(Spacer(1, 12))

    trend_text = '''
    Agricultural factors operate on different scales, so they are standardized
    to allow fair comparison over time.
    <br/><br/>

    This graph shows how each factor changes relative to its own history.
    While inputs such as irrigation and fertilizer steadily increase, crop
    yield does not follow the same upward pattern.
    <br/><br/>

    The widening gap suggests declining system efficiency, where more input
    is required just to maintain output.
    '''

    story.append(Paragraph(trend_text, styles["Normal"]))
    story.append(Spacer(1, 20))

    if graph_standardized.exists():
        img = Image(str(graph_standardized), width=450, height=220)
        story.append(img)

    story.append(Spacer(1, 25))
    story.append(Paragraph(
        "Which Factors Matter Most?",
        styles["Heading3"]
    ))
    story.append(Spacer(1, 10))

    factor_text = '''
    Trend lines show movement over time, but they do not reveal impact.
    <br/><br/>

    This chart shows the relative importance of each factor in driving yield.
    Larger bars indicate stronger influence, regardless of direction.
    '''

    story.append(Paragraph(factor_text, styles["Normal"]))
    story.append(Spacer(1, 15))

    factor_graph = Path("outputs/graphs/factor_contributions.png")

    if factor_graph.exists():
        img = Image(str(factor_graph), width=450, height=220)
        story.append(img)

# --------------------------------------------------
# PAGE 5 END
# --------------------------------------------------

    story.append(PageBreak())

# --------------------------------------------------
# PAGE 5 START
# --------------------------------------------------

    story.append(Paragraph("Baseline Future: If Nothing Changes", styles["Heading1"]))
    story.append(Spacer(1, 10))

    baseline_text = '''
    The baseline future shows what happens if current trends continue without
    any major changes.
    <br/><br/>

    This scenario assumes:
    <br/>
    • no new technologies<br/>
    • no coordinated improvement efforts
    <br/><br/>

    Under these assumptions:
    <br/>
    • rainfall follows long-term climate drift<br/>
    • temperature continues to rise slowly<br/>
    • soil quality degrades gradually<br/>
    <br/><br/>

    As a result:
    <br/>
    • crop yield becomes more unstable over time<br/>
    • poor years become more frequent<br/>
    • overall yield shows a gradual downward trend
    <br/><br/>
    '''

    story.append(Paragraph(baseline_text, styles["Normal"]))

    story.append(Spacer(1, 10))

    story.append(Paragraph("Best-Case Scenario: Coordinated 1% Improvements", styles["Heading1"]))
    story.append(Spacer(1, 10))

    scenario_text = '''
    To test whether decline is unavoidable, the system evaluates a best-case
    scenario based on small but sustained improvements.
    <br/><br/>

    In this scenario, multiple factors improve together every year:
    <br/>
    • rainfall effectiveness increases slightly<br/>
    • temperature stress is reduced<br/>
    • soil health improves<br/>
    • irrigation coverage expands<br/>
    • fertilizer use becomes more efficient
    <br/><br/>

    Each change is modest just 1% per year but applied consistently.
    <br/><br/>

    Compared to the baseline future:
    <br/>
    • yield decline slows down<br/>
    • average yield remains higher over time
    <br/><br/>

    The takeaway is clear : The system is under stress, but it is not beyond
    repair. Coordinated sustained action can still change long-term outcomes.
    '''

    story.append(Paragraph(scenario_text, styles["Normal"]))
    story.append(Spacer(1, 20))

    scenario_graph = Path("outputs/graphs/baseline_vs_best_case.png")

    if scenario_graph.exists():
        img = Image(str(scenario_graph), width=450, height=220)
        story.append(img)

# --------------------------------------------------
# PAGE 5 END
# --------------------------------------------------

    story.append(PageBreak())

# --------------------------------------------------
# PAGE 6 START
# --------------------------------------------------

    story.append(Paragraph("Conclusions and Limitations", styles["Heading1"]))
    story.append(Spacer(1, 12))

    conclusion_text = '''
    This simulation provides a clear picture of how agricultural systems behave
    under long-term stress. It does not focus on individual good or bad years.
    Instead, it highlights structural patterns that emerge over time.
    <br/><br/>

    <b>Main conclusions</b>
    <br/>
    • long-term environmental stress plays a dominant role in yield outcomes<br/>
    • yield decline is not caused by one single factor<br/>
    • multiple small pressures combine to reduce system efficiency<br/>
    • increasing inputs alone does not guarantee stable productivity<br/>
    • yield instability is as important as yield decline<br/>
    • risk increases as variability grows
    <br/><br/>

    <b>Key insights from the analysis</b>
    <br/>
    • irrigation and fertilizer inputs increase steadily over time<br/>
    • yield does not increase at the same rate<br/>
    • the system works harder just to maintain output<br/>
    • good years still occur but become less reliable<br/>
    • poor years become more frequent
    <br/><br/>

    <b>What this system is designed to do</b>
    <br/>
    • study long-term trends rather than short-term noise<br/>
    • compare baseline futures with intervention scenarios<br/>
    • identify which factors matter most for yield behavior<br/>
    • remain transparent and easy to interpret
    <br/><br/>

    <b>Limitations of the approach</b>
    <br/>
    • the model is linear by design<br/>
    • non-linear feedback effects are not included<br/>
    • regional crop differences are not modeled<br/>
    • results are based on synthetic data<br/>
    • values represent trends not exact predictions
    <br/><br/>

    <b>Future directions</b>
    <br/>
    • integrate real agricultural datasets<br/>
    • expand scenario design and testing<br/>
    • include additional stress factors where possible<br/>
    • build interactive tools for exploration and education
    '''

    story.append(Paragraph(conclusion_text, styles["Normal"]))

    story.append(Spacer(1, 85))

    reference_text = """
    <b>References and Project Resources</b>
    <br/><br/>

    For readers who want a deeper understanding of how the system works,
    the complete project code and explanations are publicly available.
    <br/><br/>

    <b>Interactive notebook (recommended)</b>
    <br/>
    A well-documented Jupyter notebook that explains the full pipeline,
    step by step, with code, outputs, and reasoning.
    <br/>
    <a href="https://github.com/Abhinav08bhatt/AgriTrend_simulation/blob/main/notebooks/documentation_code.ipynb">
    https://github.com/Abhinav08bhatt/AgriTrend_simulation/blob/main/notebooks/documentation_code.ipynb
    </a>
    <br/><br/>

    <b>Project repository</b>
    <br/>
    Complete source code, modular structure, graphs, and report generation scripts.
    <br/>
    <a href="https://github.com/Abhinav08bhatt/AgriTrend_simulation/tree/main">
    https://github.com/Abhinav08bhatt/AgriTrend_simulation/tree/main
    </a>
    <br/><br/>

    These resources are intended for transparency, reproducibility,
    and further exploration of the ideas presented in this report.
    """

    story.append(Paragraph(reference_text, styles["Normal"]))


# --------------------------------------------------
# PAGE 6 END
# --------------------------------------------------

    doc.build(story)
