from .graph.builder import build_graph



def main():
    graph = build_graph()
    result = graph.invoke({
        "message": "Hello, what is your name?",
        "response": ""
    })
    
    print(result['response'])  # Print the response content from the graph invocation
    
    
    
if __name__ == "__main__":
    main()    
    