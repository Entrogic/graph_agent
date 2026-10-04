                 LangGraph Persistence
                         │
              ┌──────────┴──────────┐
              │                     │
         Checkpointer              Store
              │                     │
        Short-term memory      Long-term memory
              │                     │
        One thread             Multiple threads
              │                     │
     Conversation state       User preferences
     Graph state              Facts
     Messages                 Shared knowledge