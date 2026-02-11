# Rules for AI Coding Assistants

## Core Principles

1. **Problem-Solving Awareness**
   - Recognize when continuing with the current approach would be counterproductive
   - Propose more fundamental solutions when appropriate
   - Maintain awareness of the broader codebase context
   - Be aware of AI's tendency to persist with repetitive approaches
   - Look for opportunities in tasks previously considered "too much work"
   - Be aware of AI's knowledge limitations and cutoff dates
   - Recognize when documentation needs to be consulted
   - Prioritize getting end-to-end systems working before optimization
   - Consider type system tradeoffs in language selection

2. **Information and Context Management**
   - Respect information hiding boundaries in testing and implementation
   - Avoid overfitting on internal implementation details
   - Preserve intended redundancy in test files when it serves a purpose
   - Keep files small to respect AI tool context limitations
   - Consider file size impact on RAG systems and IDE performance
   - Keep all tool invocations stateless and independent
   - Avoid relying on state that persists between invocations
   - Structure project setup to enable commands to run from a single directory
   - Minimize directory changes during command execution
   - Prefer stateless tool commands over stateful ones
   - Monitor file sizes to prevent context window overflow
   - Respect information hiding boundaries when loading files into context
   - Provide relevant documentation when working with unfamiliar frameworks
   - Be aware of AI's knowledge cutoff and potential hallucinations
   - Focus on getting basic end-to-end functionality working first
   - Ensure type errors are properly communicated to the AI

3. **Change Management**
   - Decompose complex changes into smaller, focused steps
   - Prioritize preparatory refactoring before making functional changes
   - Keep changes focused on the specific task at hand
   - Avoid making unrelated improvements during task execution
   - Consider using brute force approaches for large-scale refactoring when appropriate
   - Break down large files before making significant changes
   - Consider IDE and AI tool limitations when planning changes
   - Verify framework-specific changes against documentation
   - Implement walking skeleton before optimizing components
   - Get end-to-end functionality working before improvements
   - Consider type system impact on refactoring decisions
   - Monitor type errors during changes to identify affected files

4. **Automation and Efficiency**
   - Leverage AI's ability to handle repetitive tasks efficiently
   - Use brute force approaches when they can be automated effectively
   - Monitor for patterns of repetitive behavior that could be improved
   - Build workflows for handling large-scale automated changes
   - Regularly evaluate if a more efficient approach is possible
   - Use automated tools for mechanical tasks like formatting and linting
   - Save LLM capacity for complex tasks that require reasoning
   - Use AI to handle the drudgery of managing imports in split files
   - Prefer automated linting tools over manual fixes
   - Leverage AI's knowledge of common frameworks when appropriate
   - Focus on getting basic functionality working before optimization
   - Use AI to handle type system boilerplate
   - Consider token costs when making type-related changes

5. **Requirement and Communication Management**
   - Focus on clearly articulating requirements before proposing solutions
   - Specify all constraints and custom requirements explicitly
   - Be aware that AI will fill unspecified requirements with training data defaults
   - When requirements are misunderstood, edit the original prompt rather than continuing
   - Clearly communicate any solution aspects that must work in a specific way
   - Verify that specified solution requirements are appropriate and necessary
   - Document all requirements, constraints, and assumptions
   - Be explicit about potential impacts and reasoning behind changes
   - Consider file size constraints in requirements planning
   - Communicate when documentation needs to be consulted
   - Be transparent about AI's knowledge limitations
   - Prioritize end-to-end functionality in requirements
   - Consider type system requirements in language selection
   - Communicate type-related constraints and tradeoffs

## Implementation Guidelines

### 1. Tool Usage and Environment Setup
- Use agent mode and MCP servers when available for better tool interaction
- Keep all commands stateless and independent
- Avoid relying on shell state between commands
- Structure commands to work from a single directory
- Minimize directory changes during execution
- When directory changes are necessary, explicitly state and track them
- Consider using workspace-specific contexts for different project components
- Build automated workflows for repetitive command sequences
- Monitor file sizes to prevent context window limitations
- Verify framework-specific commands against documentation
- Be aware of tool-specific limitations and requirements
- Focus on getting basic commands working before optimization
- Configure type checking tools appropriately
- Monitor type checking results during changes
- Document command patterns and requirements
- Consider security implications of command execution

### 2. Code Organization and Structure
- Break down complex tasks into smaller, manageable steps
- Validate assumptions early in the process
- When encountering unexpected complexity, pause to reassess the approach
- Document the reasoning behind proposed changes and alternative approaches
- Keep changes focused and avoid scope creep
- Structure project layout to minimize directory changes
- Consider architectural dependencies and their impact on the current task
- Ensure each change is independently reviewable
- Consider using automated approaches for large-scale structural changes
- Use appropriate automated formatting tools (e.g., gofmt, rustfmt, black) for code style
- Keep files under 64KB to ensure reliable IDE patch application
- Split large files before making significant changes
- Consider single responsibility principle when organizing code
- Verify framework-specific patterns against documentation
- Implement walking skeleton before optimizing structure
- Configure type checker settings appropriately
- Consider type system impact on code organization

### 3. Testing and Quality
- Follow black box testing principles when appropriate
- Preserve test redundancy when it helps catch implementation bugs
- Avoid making tests dependent on implementation details
- Maintain test independence from implementation specifics
- Keep hard-coded test values when they serve a specific testing purpose
- When dealing with tests or features involving randomness:
  - Verify if the implementation should be deterministic
  - If nondeterminism is causing issues, propose making the implementation deterministic
  - Maintain test stability by ensuring deterministic behavior when appropriate
- Avoid over-optimization of test code at the expense of test effectiveness
- Use automated approaches for updating test values when appropriate
- Keep test files small to ensure reliable AI tool operation
- Verify framework-specific testing patterns against documentation
- Focus on basic end-to-end testing before comprehensive coverage
- Consider type system impact on test design
- Use type checking as part of quality assurance

### 4. Refactoring and Changes
- Before proceeding with implementation:
  - Identify prerequisite features or refactoring that should be done first
  - If prerequisites are found, explicitly state them and recommend addressing them
  - Propose preparatory refactoring as separate, focused changes
  - Ensure refactoring changes are semantics-preserving
  - Consider splitting large files before making changes
  - Consult documentation for framework-specific refactoring patterns
  - Get basic functionality working before refactoring
  - Consider type system impact on refactoring
- When evaluating solutions:
  - If current solution requires multiple workarounds, evaluate if a more fundamental approach exists
  - When a simpler, more robust solution is possible, propose it
  - Resist the urge to make unrelated improvements while working on a specific task
  - Verify solutions against framework documentation
  - Prioritize working solutions over elegant ones initially
  - Consider type system tradeoffs in solution design
- For large-scale refactoring:
  - Consider using automated approaches for systematic changes
  - Build workflows for handling cascading changes
  - Monitor for patterns that could be addressed more efficiently
  - Regularly evaluate if the current approach is optimal
  - Break down large files before refactoring
  - Ensure framework-specific patterns are followed
  - Get end-to-end functionality working before optimization
  - Monitor type errors during large-scale changes

### 5. Communication and Documentation
- When detecting a problematic situation:
  - Clearly explain why the current approach may not be optimal
  - Present alternative approaches with their benefits and trade-offs
  - Let the user decide whether to continue or pivot
- Be explicit about:
  - Potential impacts of proposed changes
  - State changes or directory movements during execution
  - Reasoning behind proposed changes and alternatives
  - File size considerations and limitations
  - Need for documentation consultation
  - AI's knowledge limitations
  - Focus on getting basic functionality working first
  - Type system considerations and tradeoffs
  - Tool interaction patterns and requirements
- Clearly separate refactoring proposals from functional changes
- Document automated workflows and their expected outcomes
- Explain when brute force approaches are being used and why
- When requirements are misunderstood:
  - Edit the original prompt rather than continuing with corrections
  - Explain why the original requirements were not met
  - Propose how to better specify the requirements
- Document when documentation needs to be consulted
- Be transparent about potential hallucinations or knowledge limitations
- Communicate the walking skeleton approach when appropriate
- Document type system configuration and requirements
- Document tool interaction patterns and requirements

### 6. Requirement Management
- Before starting implementation:
  - List all explicit requirements and constraints
  - Identify any implicit requirements that need to be made explicit
  - Specify any solution aspects that must work in a particular way
  - Document any assumptions about the solution space
  - Consider file size constraints in requirements
  - Identify documentation needs for framework-specific requirements
  - Prioritize end-to-end functionality requirements
  - Consider type system requirements and tradeoffs
  - Specify tool interaction requirements
- During implementation:
  - Monitor for requirement misunderstandings
  - Be prepared to restart with clearer requirements if needed
  - Validate that solutions meet all specified requirements
  - Monitor file sizes and split files when necessary
  - Verify framework-specific requirements against documentation
  - Focus on getting basic functionality working first
  - Monitor type system compliance
  - Monitor tool interaction patterns
- After implementation:
  - Verify that all requirements are satisfied
  - Document any discovered implicit requirements
  - Note any requirements that were modified during implementation
  - Document any framework-specific considerations that emerged
  - Plan improvements after basic functionality is working
  - Document type system considerations and decisions
  - Document tool interaction patterns 