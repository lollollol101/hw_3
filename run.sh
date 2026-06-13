case "$1" in
    build_generator)
        docker build -f Dockerfile -t generator-image .
        ;;
    run_generator)
        docker run --rm -v $(pwd)/data:/data generator-image
        ;;
    create_local_data)
        python generate.py ./local_data
        ;;
    build_reporter)
        docker build -f Dockerfile.reporter -t reporter-image .
        ;;
    run_reporter)
        docker run --rm -v $(pwd)/data:/data reporter-image
        ;;
esac