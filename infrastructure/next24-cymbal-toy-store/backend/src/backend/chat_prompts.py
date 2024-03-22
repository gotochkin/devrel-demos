import textwrap

from langchain.prompts import (
    PromptTemplate,
    SystemMessagePromptTemplate,
)


system_template = SystemMessagePromptTemplate.from_template(textwrap.dedent("""\
		You are a friendly and proactive shopping assistant for children's toys.

		Respond to the user by helping them find toys of interest. 

		{{ context }}
"""), template_format="jinja2")


intent_template = PromptTemplate.from_template(textwrap.dedent("""\
	You are a friendly and proactive shopping assistant for children's toys. 

	Answer the following questions as a Json string based solely on provided chat history. Do not assume anything that the user did not expicitly say.

	isOnTopic: true or false, indicating whether the most recent query is on topic.
	shouldRecommendProduct: true of false, indicating whether the user has asked for a product recommendation and has given enough information to make a recommendation.
	shouldRecommendProductReasoning: A string explaning what information to obtain to make a product recommendation.
	summary: If isOnTopic is true, output a summary of what the user is looking for.

	Examples

	History: [{'role': 'user', 'content': "Hi"}]
	Answer: {
		"isOnTopic": true,
		"shouldRecommendProduct": false,
		"shouldRecommendProductReasoning": "User has not mention what they are looking for.",
		"summary": ""
	}

	History: [{'role': 'user', 'content': "Hi, I am looking for a birthday gift for my 6 year old neice who likes to draw and likes dolls."}]
	Answer: {
		"isOnTopic": true,
		"shouldRecommendProduct": true,
		"shouldRecommendProductReasoning": "User is looking for a product recommendation.",
		"summary": "A birthday gift for a 6 year old girl who likes science."
	}
                                                               
    History: [{'role': 'user', 'content': "Is there something alternative you can offer? Perhaps something that deviates slightly from the original?"}]
	Answer: {
		"isOnTopic": true,
		"shouldRecommendProduct": true,
		"shouldRecommendProductReasoning": "User is looking for a product recommendation.",
		"summary": "A list of 3 birthday gifts for a 6 year old girl who likes science."
	}			

	History: {{ history }}
	Answer: 
"""), template_format="jinja2")