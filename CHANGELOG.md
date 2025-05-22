# Changelog

## 1.0.1 (2025-05-22)

Full Changelog: [v1.0.0...v1.0.1](https://github.com/nptakudo/stainless-api-sdk/compare/v1.0.0...v1.0.1)

### Bug Fixes

* **package:** support direct resource imports ([e3ba01e](https://github.com/nptakudo/stainless-api-sdk/commit/e3ba01ef5bd391b772f6802ef89e75bba5df9a9d))
* **perf:** optimize some hot paths ([7316ff5](https://github.com/nptakudo/stainless-api-sdk/commit/7316ff538ca7a831869376024c6f2374099e082a))
* **perf:** skip traversing types for NotGiven values ([bec8691](https://github.com/nptakudo/stainless-api-sdk/commit/bec8691846d2c722c29d8c6ede018b1d44e97a7f))
* **pydantic v1:** more robust ModelField.annotation check ([417864d](https://github.com/nptakudo/stainless-api-sdk/commit/417864dfce89e6b71d48aeedc7cded1d59d34bc1))


### Chores

* broadly detect json family of content-type headers ([0c9d6ba](https://github.com/nptakudo/stainless-api-sdk/commit/0c9d6ba9e74301d121f46113d3e9ec766be56587))
* **ci:** add timeout thresholds for CI jobs ([1f0ba96](https://github.com/nptakudo/stainless-api-sdk/commit/1f0ba96072f0775d74a7110191988122a9c31378))
* **ci:** fix installation instructions ([8ea9fbf](https://github.com/nptakudo/stainless-api-sdk/commit/8ea9fbfd86692c5938d88c245806c475f0684638))
* **ci:** only use depot for staging repos ([d40a0be](https://github.com/nptakudo/stainless-api-sdk/commit/d40a0be46a738501c7de89d9440ba53e3c2996c5))
* **ci:** upload sdks to package manager ([a6e01b1](https://github.com/nptakudo/stainless-api-sdk/commit/a6e01b14006e7a071702725873ef0dff192691e0))
* **client:** minor internal fixes ([21ff6f4](https://github.com/nptakudo/stainless-api-sdk/commit/21ff6f4cd9bb34c67f8e1fe626140a61215d8057))
* **docs:** grammar improvements ([6d5d621](https://github.com/nptakudo/stainless-api-sdk/commit/6d5d621f07e04f543e350db584a8c6a951291281))
* fix typos ([#5](https://github.com/nptakudo/stainless-api-sdk/issues/5)) ([eb96a57](https://github.com/nptakudo/stainless-api-sdk/commit/eb96a57bb33082fd71a99662444c8c0d717e8042))
* **internal:** avoid errors for isinstance checks on proxies ([af24a6b](https://github.com/nptakudo/stainless-api-sdk/commit/af24a6b58d6c8adfc777e5fcecbd452f9977a393))
* **internal:** base client updates ([ea770fc](https://github.com/nptakudo/stainless-api-sdk/commit/ea770fcb70f0049ce390c1c9e14f9c852a8d6626))
* **internal:** bump pyright version ([50bcf19](https://github.com/nptakudo/stainless-api-sdk/commit/50bcf197db67cea2681c54f1e4b6fab9daf21744))
* **internal:** codegen related update ([931f0c2](https://github.com/nptakudo/stainless-api-sdk/commit/931f0c2079e85223424b91e3a68482bb69a28f10))
* **internal:** expand CI branch coverage ([9cb57ab](https://github.com/nptakudo/stainless-api-sdk/commit/9cb57ab06a5671a4545cf57148f12730e89b873f))
* **internal:** fix list file params ([def4f15](https://github.com/nptakudo/stainless-api-sdk/commit/def4f1523f73772f4aa2b16af8abc75d9168510d))
* **internal:** import reformatting ([4351d23](https://github.com/nptakudo/stainless-api-sdk/commit/4351d2356b39a9ff883c343f4c21a2c71b365039))
* **internal:** minor test fixes ([#7](https://github.com/nptakudo/stainless-api-sdk/issues/7)) ([9adf244](https://github.com/nptakudo/stainless-api-sdk/commit/9adf244935fdcb18d0d7601e25452e248a380034))
* **internal:** reduce CI branch coverage ([7c137a3](https://github.com/nptakudo/stainless-api-sdk/commit/7c137a3362fa6afd9d3281e6fccf493adccd6de5))
* **internal:** refactor retries to not use recursion ([aa45d61](https://github.com/nptakudo/stainless-api-sdk/commit/aa45d61eedecec3a73d609a56afeaeb87b1f97d2))
* **internal:** remove trailing character ([#8](https://github.com/nptakudo/stainless-api-sdk/issues/8)) ([cbc2014](https://github.com/nptakudo/stainless-api-sdk/commit/cbc201425ef037e04dbb8cdb7a23b50b37d5925f))
* **internal:** slight transform perf improvement ([#10](https://github.com/nptakudo/stainless-api-sdk/issues/10)) ([dd9184e](https://github.com/nptakudo/stainless-api-sdk/commit/dd9184e8bed57be88d8e329ad673dfab04f1f59a))
* **internal:** update models test ([b3fe44f](https://github.com/nptakudo/stainless-api-sdk/commit/b3fe44f33d61a318afa9d57811a3cfa2200eddef))
* **internal:** update pyright settings ([df4010f](https://github.com/nptakudo/stainless-api-sdk/commit/df4010f5d47766fdd4c4bb5da1b81be3d6caf7f1))
* **tests:** improve enum examples ([#11](https://github.com/nptakudo/stainless-api-sdk/issues/11)) ([98b7337](https://github.com/nptakudo/stainless-api-sdk/commit/98b7337b611ee3c0e531e28c691eaa4d5d37efe6))


### Documentation

* swap examples used in readme ([#9](https://github.com/nptakudo/stainless-api-sdk/issues/9)) ([6d72b61](https://github.com/nptakudo/stainless-api-sdk/commit/6d72b61c04c6fcfe1d3babe376d4f1636e2fc531))

## 1.0.0 (2025-03-25)

Full Changelog: [v0.0.1-alpha.0...v1.0.0](https://github.com/nptakudo/stainless-api-sdk/compare/v0.0.1-alpha.0...v1.0.0)

### Chores

* go live ([#1](https://github.com/nptakudo/stainless-api-sdk/issues/1)) ([38d0445](https://github.com/nptakudo/stainless-api-sdk/commit/38d04454411778de895effbbd7f3e96b80a61927))
* update SDK settings ([#3](https://github.com/nptakudo/stainless-api-sdk/issues/3)) ([ebc0461](https://github.com/nptakudo/stainless-api-sdk/commit/ebc0461a1cc4e3a047088ce31ee40a0371b5131f))
