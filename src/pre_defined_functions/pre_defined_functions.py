class PreDefinedFunctions():
    functions = [
        {
            "print": {
                "return_type": "void",
                "parameters": [
                    {
                        "type": "string",
                        "name": "value"
                    }
                ]
            }
        },
        {
            "bool_to_string": {
                "return_type": "string",
                "parameters": [
                    {
                        "type": "bool",
                        "name": "value"
                    }
                ]
            }
        },
        # {
        #     "num_to_string": {
        #         "return_type": "string",
        #     }
        # },
    ]
