mkdir -p ~/.streamlit/


# shellcheck disable=SC1073
# shellcheck disable=SC1009
echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\" > ~/.streamlit/config.toml
