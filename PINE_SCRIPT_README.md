# AI-Inspired Trading Strategy (Pine Script)

This repository now includes a Pine Script file (`ai_trading_strategy.pine`) containing an advanced AI-inspired trading strategy for TradingView.

## Pine Script Features

### 📊 Technical Indicators
- **Moving Averages**: Fast (9-period) and Slow (21-period) EMAs
- **RSI**: 14-period Relative Strength Index with scoring system
- **MACD**: Moving Average Convergence Divergence with signal evaluation
- **Ichimoku Cloud**: Complete cloud analysis with multiple components
- **Volume Analysis**: Volume comparison with 20-period moving average

### 🤖 AI Decision Engine
The strategy combines multiple technical indicators using configurable weights:
- RSI Weight: 25% (default)
- MACD Weight: 20% (default) 
- Ichimoku Weight: 30% (default)
- Volume Weight: 15% (default)
- Sentiment Weight: 10% (default)

### 🎯 Trade Management System
- **Position Tracking**: Monitors active positions and trade history
- **Risk Management**: Configurable stop-loss and take-profit levels
- **Trailing Stops**: Dynamic trailing stop-loss adjustments
- **Partial Exits**: Option to take partial profits at configurable levels

### 🚦 Enhanced Exit Signals
Multiple exit conditions with strength levels:
- Trend Reversal Exit
- Technical Indicator Exit
- Stop Loss Exit
- Take Profit Exit
- Momentum Fading Exit
- Drawdown Protection Exit

### 📈 Visual Features
- **Interactive Charts**: EMA lines and Ichimoku cloud visualization
- **Signal Markers**: Buy/sell signals with distinct icons
- **Exit Indicators**: Various exit signal types with unique visuals
- **Live Status Table**: Real-time market condition and position status
- **Dynamic Lines**: Entry, stop-loss, take-profit, and partial profit levels

### ⚠️ Alert System
Comprehensive alert conditions for:
- Buy/Sell signals
- Stop loss hits
- Take profit targets
- Urgent exit requirements
- Partial profit opportunities

## Usage Instructions

1. Copy the content of `ai_trading_strategy.pine`
2. Open TradingView Pine Editor
3. Paste the code and save as a new indicator
4. Apply to any chart and configure the input parameters
5. Set up alerts for automated notifications

## Configuration Options

### Exit Signal Settings
- Exit Signal Visibility (Low/Medium/High)
- Show Take Profit Levels (boolean)
- Show Exit Arrows (boolean)
- Exit Signal Lookback (1-20 bars)
- Partial Exit % (0.5-10.0%)
- Full Exit % (1.0-20.0%)

### Live Market Settings
- Risk/Reward Ratio (0.5-5.0)
- Trailing Stop % (0.5-10.0%)
- Take Profit % (1.0-20.0%)

### AI Weights
All weights are adjustable from 0 to 1 in 0.05 increments:
- RSI Weight
- MACD Weight  
- Ichimoku Weight
- Volume Weight
- Sentiment Weight

## File Structure
```
├── ai_trading_strategy.pine    # Complete Pine Script trading strategy
├── PINE_SCRIPT_README.md      # This documentation file
└── [other repository files]   # Original planar graph visualizer files
```

## Note
This Pine Script is independent of the main planar graph visualization application and is provided as an additional resource for trading analysis on the TradingView platform.