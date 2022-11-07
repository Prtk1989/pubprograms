

Output: 
{ 
  "pcs-ing-aws-rit-management":
    [
	{ "rl-pcs-ing-aws-rit-management": "redlock/pcs-ddi-rit-management:VAC-FSI-22.7.2-RC4"},
	{"s3-files-sync-service": "redlock/rit-sync-service:390803b51fe89a369fa942fdaf560ec6e6a8c1b7"}
    ],
  "service2": []
}
=====================
{
    "pcs-ing-aws-rit-management":
    [
        {
            "namespace": "ingestion-aws",
            "podname": "pcs-ing-aws-rit-management-5cf876cffd-d2dsq",
            "helm_chart": null,
            "containers":
            [
                {
                    "rl-pcs-ing-aws-rit-management":
                    {
                        "image": "redlock/pcs-ddi-rit-management:VAC-FSI-22.7.2-RC4",
                        "restart_count": 0,
                        "ready": true,
                        "state": "Running"
                    }
                },
                {
                    "s3-files-sync-service":
                    {
                        "image": "redlock/rit-sync-service:390803b51fe89a369fa942fdaf560ec6e6a8c1b7",
                        "restart_count": 0,
                        "ready": true,
                        "state": "Running"
                    }
                }
            ],
            "init_containers": null,
            "containersUp": "2/2",
            "pod_status": "RUNNING",
            "start_time": "2022-07-28 17:02:43"
        }
    ],
    "pcs-ing-aws-rit-ordinator":
    [
        {
            "namespace": "ingestion-aws",
            "podname": "pcs-ing-aws-rit-ordinator-56746679b8-xd2qn",
            "helm_chart": null,
            "containers":
            [
                {
                    "rl-pcs-ing-aws-rit-ordinator":
                    {
                        "image": "redlock/pcs-ddi-job-ordinator:VAC-FSI-22.7.2-RC4",
                        "restart_count": 0,
                        "ready": true,
                        "state": "Running"
                    }
                }
            ],
            "init_containers": null,
            "containersUp": "1/1",
            "pod_status": "RUNNING",
            "start_time": "2022-07-26 13:52:27"
        }
    ],
    "pcs-ing-aws-rit-scheduler":
    [
        {
            "namespace": "ingestion-aws",
            "podname": "pcs-ing-aws-rit-scheduler-6b76d84879-d79vh",
            "helm_chart": null,
            "containers":
            [
                {
                    "rl-pcs-ing-aws-rit-scheduler":
                    {
                        "image": "redlock/pcs-ddi-job-scheduler:VAC-FSI-22.7.2-RC4",
                        "restart_count": 0,
                        "ready": true,
                        "state": "Running"
                    }
                }
            ],
            "init_containers":
            [
                {
                    "auth-user":
                    {
                        "image": "redlock/curl-jq:latest",
                        "restart_count": 0,
                        "ready": true
                    }
                }
            ],
            "containersUp": "1/1",
            "pod_status": "RUNNING",
            "start_time": "2022-07-26 13:52:28"
        }
    ]
}
