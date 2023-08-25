part 1:
	downloaded docker desktop for windows
	ran nginx container: docker run -d --name nginx_container -p 669:80 nginx
	ran prometheus exporter: docker run -d --name nginx_exporter_container -p 9113:9113 -e NGINX_SCRAPE_URI=http://host.docker.internal:669/nginx_status nginx/nginx-prometheus-exporter
	ran promethues container with custom "prometheus.yml": docker run -d --name prometheus_container -p 9090:9090 -v C:\path\to\prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
	ran grafana container: docker run -d --name grafana_container -p 3000:3000 grafana/grafana
	imported grafana dashboard "nginx exporter" from the official site

part 2: 
	created the files as shown
	executed: docker-compose up

part 3:
	run find_duplicate_files.py /your_directory/