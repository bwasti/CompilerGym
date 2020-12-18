// Copyright (c) Facebook, Inc. and its affiliates.
//
// This source code is licensed under the MIT license found in the
// LICENSE file in the root directory of this source tree.
#pragma once

#include "compiler_gym/service/proto/compiler_gym_service.pb.h"

namespace compiler_gym::llvm_service {

// This generated file defines the LlvmAction enum which lists the available
// LLVM transforms. Generated by //compiler_gym/envs/llvm/service/passes:action-genfiles.
#include "compiler_gym/envs/llvm/service/passes/ActionEnum.h"  // @donotremove

// The available action spaces for LLVM.
//
// NOTE(cummins): Housekeeping rules - to add a new action space:
//   1. Add a new entry to this LlvmActionSpace enum.
//   2. Add a new switch case to getLlvmActionSpaceList() to return the
//      ActionSpace.
//   3. Add a new switch case to LlvmEnvironment::takeAction() to compute
//      the actual action.
//   4. Run `bazel test //compiler_gym/...` and update the newly failing tests.
enum class LlvmActionSpace {
  // The full set of transform passes for LLVM.
  PASSES_ALL,
};

// Get the list of LLVM action spaces.
std::vector<ActionSpace> getLlvmActionSpaceList();

}  // namespace compiler_gym::llvm_service
