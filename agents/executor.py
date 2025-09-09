
from tools import email_sender, web_scraper, pdf_summarizer
from memory.local_memory import LocalMemory

tool_map = {
    "send_email": email_sender.send_email,
    "scrape_website": web_scraper.scrape_website,
    "summarize_text": pdf_summarizer.summarize_text
}

memory = LocalMemory()

def substitute_variables(input_data, previous_outputs):
    if isinstance(input_data, dict):
        for key, value in input_data.items():
            if isinstance(value, str) and value.startswith("{{") and value.endswith("}}"):
                var_name = value[2:-2].strip()
                for output in reversed(previous_outputs):
                    if var_name in output:
                        input_data[key] = output[var_name]
                        break
    return input_data

def execute_workflow(workflow):
    results = []
    for step in workflow.steps:
        tool_name = step.tool
        inputs = step.input
        inputs = substitute_variables(inputs, results)

        func = tool_map.get(tool_name)
        if func:
            result = func(**inputs)
            results.append(result)
            memory.save(tool_name, result)
        else:
            results.append({"error": f"Tool {tool_name} not found"})
    return results
