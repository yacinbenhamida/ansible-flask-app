#!/bin/bash
systemctl daemon-reload
systemctl start flask
systemctl enable flask
systemctl restart nginx