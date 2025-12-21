from flask import Blueprint, flash,redirect,url_for,request, render_template,jsonify
from models.chatModel import ask_ai

chatbot_bp =Blueprint('chatbot_bp',__name__)

@chatbot_bp.route('/chatbot')
def chatbot():

    return render_template("chatbot.html")

@chatbot_bp.route('/ask', methods = ['POST','GET'])
def ask():
    data = request.json
    question = data.get("question", "")

    if not question:
        return jsonify({"error": "Question required"}), 400

    answer = ask_ai(question)

    return jsonify({"answer": answer})
