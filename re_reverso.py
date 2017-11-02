"""
Flask App to reverse lines
"""

import os
from flask import Flask, request, Response, stream_with_context
APP = Flask(__name__)

@APP.route("/reverso", methods=['POST'])
def reverso():
    """
    Endpoint that reverses every line of
    data.
    """
    def line_reverse():
        """
        Iterates over lines in data,
        reverses them, and yields.
        For streaming.
        For streaming.
        For streaming.
        For streaming.
        """
        data = request.data.decode('utf-8')
        buff = []
        for char in data:
            if char is '\n':
                yield ''.join(buff) + '\n'
                del buff[:]
            else:
                buff.insert(0, char)
        yield ''.join(buff) + '\n'

    return Response(stream_with_context(line_reverse()), mimetype='text/plain')
