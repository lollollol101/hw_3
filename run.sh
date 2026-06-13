case "$1" in
    build_generator)
        docker build -t generator-image .
        ;;
    run_generator)
        docker run --rm -v $(pwd)/data:/data generator-image
        ;;
    create_local_data)
        python generate.py ./local_data
        ;;
esac