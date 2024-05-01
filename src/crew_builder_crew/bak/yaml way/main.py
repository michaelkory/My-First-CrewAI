import os
from dotenv import load_dotenv
load_dotenv()

from crew_builder_crew.crew import CrewBuilderCrew

def run():
    inputs = {
        'new_crew_purpose': 'build a new crew builder crew',
        'new_crew_details': 'build the most excellent crewai crew for building crewai crews',
        # 'new_crew_purpose': 'build a new crew to create Jupyter notebooks',
        # 'new_crew_details': """
        #     ## 📋 Key Components
        #     ### 1. 🛠️ Setup and Data Preparation
        #     - Naming conventions and notebook structure
        #     - Required libraries: Pandas, NumPy, Matplotlib
        #     - Data loading, cleaning, and technical indicator calculations

        #     ### 2. 📈 Trading Strategy Definition
        #     - Clear entry and exit rules
        #     - Generating buy/sell signals
        #     - Avoiding look-ahead bias
        #     - 📊 Visualizations:
        #     - Price data, indicators, and trading signals
        #     - Line plots, overlay plots, and signal highlighting

        #     ### 3. 💰 Backtesting and Performance Metrics
        #     - Trade simulation based on signals
        #     - Portfolio tracking and performance metrics
        #     - Returns, volatility, Sharpe ratio, max drawdown
        #     - 📈 Visualizations:
        #     - Equity curve and drawdown periods
        #     - Cumulative returns vs buy-and-hold

        #     ### 4. 🎯 Optimization and Risk Management
        #     - Experimenting with indicator parameters
        #     - Multi-timeframe and multi-market testing
        #     - Position sizing and stop losses
        #     - Transaction cost sensitivity analysis
        #     - Systematic documentation of tests and results

        #     ## 💡 Guidelines for the AI Assistant
        #     - Use clear, concise language and well-structured code examples
        #     - Emphasize the importance of visualizations for insights
        #     - Highlight common pitfalls to avoid (e.g., overfitting)
        #     - Encourage systematic testing and documentation
        #     - Provide guidance on interpreting and communicating results

        #     ## 🎨 Formatting
        #     - Use markdown for structure and emphasis
        #     - Include emojis for visual appeal and quick reference
        #     - Provide code snippets in Python with clear explanations
        #     - Use bullet points for key concepts and action items
        # """,
        # 'new_crew_purpose': 'build a weekly Red Hat newsletter.',
        # 'new_crew_details': 'build the most excellent crewai crew for crafting a weekly Red Hat newsletter, with upcoming events, workshops, and the latest news on RHEL, OpenShift, and Ansible.'
        # 'new_crew_purpose': 'build a daily poly relationship social media strategy.',
        # 'new_crew_details': 'build the most excellent crewai crew for crafting a daily content for twitter, instagram, youtube, and tiktok, for my polyamoruous coaching business.'
    }
    CrewBuilderCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()