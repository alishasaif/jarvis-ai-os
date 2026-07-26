"""
J.A.R.V.I.S Memory Search

Searches stored memories before
sending requests to the AI model.
"""


from backend.ai.memory.memory_engine import memory_engine



class MemorySearch:


    def search(self, query: str):

        query = query.lower()


        data = memory_engine.recall()


        results = []


        # Search preferences

        preferences = data.get(
            "preferences",
            {}
        )


        for key, value in preferences.items():

            if (
                key.replace("_", " ")
                in query
                or key in query
            ):

                results.append({

                    "key": key,

                    "value": value

                })


        # Search profile

        profile = data.get(
            "profile",
            {}
        )


        for key, value in profile.items():

            if (
                key.replace("_", " ")
                in query
                or key in query
            ):

                results.append({

                    "key": key,

                    "value": value

                })


        # Search general memory

        for key, value in data.items():

            if isinstance(value, str):

                if key in query:

                    results.append({

                        "key": key,

                        "value": value

                    })


        return results



    def answer(self, query):

        results = self.search(
            query
        )


        if not results:

            return None


        memory = results[0]


        return (
            f"Your {memory['key'].replace('_',' ')} "
            f"is {memory['value']}, Sir."
        )



memory_search = MemorySearch()