
import time
from src.config import setup_environment
from src.agents.hunter import HunterAgent
from src.agents.analyst import AnalystAgent
from src.memory.store import MemoryBank

def run_market_watch_pipeline(target_company: str, target_url: str):
    # 1. Setup
    setup_environment()
    print(f"🚀 Starting MarketWatch Agent for: {target_company}")
    
    memory = MemoryBank()
    hunter = HunterAgent()
    analyst = AnalystAgent()

    # 2. AGENT A: THE HUNTER (Gather Data)
    print("\n🕵️  Hunter Agent: Scanning target...")
    current_market_data = hunter.research(target_company, target_url)
    print(f"   > Data Found: {current_market_data}")

    # 3. MEMORY: Retrieve History & State
    print("\n🧠 Memory Bank: Retrieving historical context...")
    historical_context = memory.get_last_entry(target_company)
    if historical_context:
        print(f"   > Found history from: {historical_context['timestamp']}")
    else:
        print(f"   > No history found (First run for {target_company})")

    # 4. AGENT B: THE ANALYST (Synthesize)
    print("\n📝 Analyst Agent: Generating strategic report...")
    final_report = analyst.write_report(
        company=target_company,
        current_data=current_market_data,
        historical_context=historical_context
    )

    # 5. SAVE STATE (Loop Closure)
    print("\n💾 System: Saving run to memory...")
    memory.save_entry(target_company, current_market_data)

    return final_report

if __name__ == "__main__":
    # Example Trigger
    report = run_market_watch_pipeline(
        target_company="TechCorp", 
        target_url="https://techcorp.example.com/pricing"
    )
    
    print("\n" + "="*40)
    print("FINAL EXECUTIVE SUMMARY")
    print("="*40)
    print(report)